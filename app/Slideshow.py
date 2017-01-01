#!/usr/bin/python

from __future__ import absolute_import, division, print_function, unicode_literals
import pyinotify
import random, time, os, shutil, subprocess, sys, glob
#sys.path.insert(1, '/home/pi/pi3d_demos')
import pi3d

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

try:
    files = glob.glob('/home/pi/slideshow/*')
    for f in files:
        os.remove(f)
        print ("cleaning "+f)
    print ("CLEANUP OF HOTFOLDER DONE")
except:
    pass
    
config = ConfigParser()
config.read('/home/pi/app/settings.ini')
PIC_DIR = config.get('folder_settings', 'PIC_DIR')
AD_DIR = config.get('folder_settings', 'AD_DIR')
TMDELAY = config.getfloat('slideshow_settings', 'TMDELAY')
NEWDELAY = config.getfloat('slideshow_settings', 'NEWDELAY') 
FADE_TM = config.getfloat('slideshow_settings', 'FADE_TM') 
SHUFFLE = config.getboolean('slideshow_settings', 'SHUFFLE')
PPS = config.getint('slideshow_settings', 'PPS')
Advertisment = config.getboolean('slideshow_settings', 'Advertisment')
AdCounter = config.getint('slideshow_settings', 'AdCounter')
ForceAdvertisment = config.getboolean('slideshow_settings', 'ForceAdvertisment')


########################################################################
# set the user variables here
########################################################################
FPS = 20       # animation frames per second
#FADE_TM = 2.0  # time for fading
TK = False     # set to true to run in tk window (have to start x server)
MIPMAP = True  # whether to anti-alias map screen pixels to image pixels
SHUFFLE = True
CHKNUM = 1    # number of picture between re-loading file list
PicCounter=-1
TEMPDELAY = 0
TEMPIMAGE = False
########################################################################
# Where the aspect ratio of the image is different from the monitor the
# gap is filled with a low alpha reflection of the image. If you want this
# to be the pure background then you can edit the file
# shaders/blend_include_fs.inc and change edge_alpha = 0.0
########################################################################


def tex_load(fname):
  ''' return a slide object
  '''
  slide = Slide()
  if not os.path.isfile(fname):
    return None
  try:
      tex = pi3d.Texture(fname, blend=True, mipmap=MIPMAP, m_repeat=True)
      xrat = DISPLAY.width/tex.ix
      yrat = DISPLAY.height/tex.iy
      if yrat < xrat:
        xrat = yrat
      wi, hi = tex.ix * xrat, tex.iy * xrat
      xi = (DISPLAY.width - wi)/2
      yi = (DISPLAY.height - hi)/2
      slide.tex = tex
      slide.dimensions = (wi, hi, xi, yi)
      return slide
  except:
     pass


def get_files():
    file_list = []
    global PicCounter, SHUFFLE, PIC_DIR_TEMP
    if (PicCounter==AdCounter and Advertisment == True):
        if glob.glob("/home/pi/advertising/*.jpg") or glob.glob("/home/pi/advertising/*.JPG"):
            print ("\x1b[0;33;40m"+"Displaying Advertisment"+"\x1b[0;37;40m")
            PIC_DIR_TEMP=AD_DIR
        else:
            Pic_DIR_TEMP="/home/pi/void/"
    elif glob.glob("/media/usb0/*.jpg") or glob.glob("/media/usb0/*.JPG"):
        print ("\x1b[0;36;40m"+"Getting Files from Slideshow Content"+"\x1b[0;37;40m")
        PIC_DIR_TEMP=PIC_DIR
    elif glob.glob("/home/pi/advertising/*.jpg") or glob.glob("/home/pi/advertising/*.JPG"):
        print ("\x1b[0;33;40m"+"Getting Files from AD-Dir"+"\x1b[0;37;40m")
        PIC_DIR_TEMP=AD_DIR
    else:
        print ("Displaying Void Image")
        PIC_DIR_TEMP="/home/pi/void/"
    
    extensions = ['.png','.jpg','.jpeg','JPG'] # can add to these
    for root, dirnames, filenames in os.walk(PIC_DIR_TEMP):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions and not 'water' in root and not filename.startswith('.'):
                file_list.append(os.path.join(root, filename)) 
    if SHUFFLE:
      #print ("Shuffel enabled")
      random.shuffle(file_list) # randomize pictures
    else:
      #print ("Shuffel disabled")
      file_list.sort() # if not suffled; sort by name
    return file_list, len(file_list) # tuple of file list, number of pictures


class Slide(object):
  def __init__(self):
    self.tex = None
    self.dimensions = None


# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(background=(0.3, 0.3, 0.3, 1.0), frames_per_second=FPS, tk=TK)

#mykeys = pi3d.Keyboard() # don't need this for picture frame but useful for testing
 
shader = [
          pi3d.Shader("shaders/blend_star"),
          pi3d.Shader("shaders/blend_holes"),
          pi3d.Shader("shaders/blend_false"),
          pi3d.Shader("shaders/blend_burn"),
          pi3d.Shader("shaders/blend_bump")
         ]

num_sh = len(shader)
iFiles, nFi = get_files()
fade = 0.0
pic_num = nFi - 1
canvas = pi3d.Canvas()
canvas.set_shader(shader[0])
CAMERA = pi3d.Camera.instance()
CAMERA.was_moved = False #to save a tiny bit of work each loop
pictr = 0 # to allow shader changing every PPS slides
shnum = 0 # shader number
nexttm = 0.0 # force next on first loop
fade_step = 1.0 / (FPS * FADE_TM)
sbg = tex_load("/home/pi/app/void.png") # initially load a background slide


while DISPLAY.loop_running():
  tm = time.time()
  if tm > nexttm + TEMPDELAY: # load next image
    #subprocess.call(["clear"])
    #print("-----------------------------")
    PicCounter += 1
    if (PicCounter>AdCounter):
        print ("RESETTING AdCounter")
        PicCounter=0
    print ("Ad Counter: "+str(AdCounter-PicCounter))
    nexttm = tm + TMDELAY
    TEMPDELAY = 0
    fade = 0.0 # reset fade to beginning
    sfg = sbg # foreground Slide set to old background    
    pic_num = (pic_num + 1) % nFi # wraps to start
    
    if glob.glob ("/home/pi/app/temp.jpg") and not TEMPIMAGE:
        if (ForceAdvertisment == True and PicCounter==AdCounter):
            print ("\x1b[0;33;40m"+"SKIPPING DISPLAYING OF NEW FILE"+"\x1b[0;37;40m")
            TEMPDELAY = 0
            if (pic_num % CHKNUM) == 0: # this will shuffle as well
                try:
                    iFiles, nFi = get_files()
                    pic_num = pic_num % nFi # just in case list is severly shortened
                except:
                    pass
            try:
                tmp_slide = tex_load(iFiles[pic_num]) # background Slide load.
            except:
                print ("\x1b[0;31;40m"+"New image busy"+"\x1b[0;37;40m")  
                pass
            print ("Loaded: "+iFiles[pic_num])
        else:
            print ("\x1b[1;32;40m"+"NEW IMAGE DETECTED"+"\x1b[0;37;40m")
            #time.sleep(0.5)
            #print ("Sleeping done")
            TEMPDELAY += NEWDELAY
            TEMPIMAGE = True
            try:
                tmp_slide = tex_load("/home/pi/app/temp.jpg")
                print ("\x1b[1;32;40m"+"Loaded: NEW IMAGE"+"\x1b[0;37;40m")
            except:
                print ("\x1b[0;31;40m"+"New image busy"+"\x1b[0;37;40m")
                pass            
            #time.sleep(0.5)
        
    else:
        print ("No new image detected.")
        TEMPDELAY = 0
        if (pic_num % CHKNUM) == 0: # this will shuffle as well
            try:
                iFiles, nFi = get_files()
                pic_num = pic_num % nFi # just in case list is severly shortened
            except:
                pass
        try:
            tmp_slide = tex_load(iFiles[pic_num]) # background Slide load.
        except:
            print ("\x1b[0;31;40m"+"New image busy"+"\x1b[0;37;40m")  
            pass
        print ("Loaded: "+iFiles[pic_num])
        
        
        
        
    if tmp_slide != None: # checking in case file delete
      sbg = tmp_slide
    canvas.set_draw_details(canvas.shader,[sfg.tex, sbg.tex]) # reset two textures
    canvas.set_2d_size(sbg.dimensions[0], sbg.dimensions[1], sbg.dimensions[2], sbg.dimensions[3])
    canvas.unif[48:54] = canvas.unif[42:48] #need to pass shader dimensions for both textures
    canvas.set_2d_size(sfg.dimensions[0], sfg.dimensions[1], sfg.dimensions[2], sfg.dimensions[3])
    pictr += 1

    
    if pictr >= PPS:# shader change Pics Per Shader
      pictr = 0
      shnum = (shnum + 1) % num_sh
      canvas.set_shader(shader[shnum])
    print("---------------------------------")
  if fade < 1.0:
    fade += fade_step # increment fade
    if fade > 1.0: # more efficient to test here than in pixel shader
      fade = 1.0
    canvas.unif[44] = fade # pass value to shader using unif list
  
  canvas.draw() # then draw it
  if glob.glob("/home/pi/app/temp.jpg") and TEMPIMAGE:
        os.remove("/home/pi/app/temp.jpg")
        TEMPIMAGE = False
        #print ("DELETING temp.jpg")
  config.read('/home/pi/app/settings.ini')
  PIC_DIR = config.get('folder_settings', 'PIC_DIR')
  AD_DIR = config.get('folder_settings', 'AD_DIR')
  TMDELAY = config.getfloat('slideshow_settings', 'TMDELAY')
  NEWDELAY = config.getfloat('slideshow_settings', 'NEWDELAY') 
  FADE_TM = config.getfloat('slideshow_settings', 'FADE_TM') 
  SHUFFLE = config.getboolean('slideshow_settings', 'SHUFFLE')
  PPS = config.getint('slideshow_settings', 'PPS')
  Advertisment = config.getboolean('slideshow_settings', 'Advertisment')
  AdCounter = config.getint('slideshow_settings', 'AdCounter')
  ForceAdvertisment = config.getboolean('slideshow_settings', 'ForceAdvertisment')
  fade_step = 1.0 / (FPS * FADE_TM)
  SHUFFLE = True
DISPLAY.destroy()



