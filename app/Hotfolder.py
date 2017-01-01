import subprocess
import shutil
import pyinotify
import time
import glob
import os

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
    
    
config = ConfigParser()
config.read('/home/pi/app/settings.ini')
Ignore_USB_Stick = config.getboolean('startup_setting', 'Ignore_USB_Stick')
    

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        print "CLOSE_WRITE event:", event.pathname
        head,tail = os.path.split(event.pathname)
        if not event.pathname.endswith((".jpg", "JPG", "jpeg", "JPEG")): 
            print ("Skipping:" +str(event.pathname))
        else:
            try:
                if not glob.glob("/media/usb0/.donotdelete.txt") or Ignore_USB_Stick == True:
                    shutil.copyfile(event.pathname,"/media/usb0/"+str(tail))
                    print "created: /media/usb/"+str(tail)
                else:
                    print "USB-Stick not present"
            except:
                print "FAILED creation: /media/usb0/"+str(tail)+" - USB-Stick not present"
                pass
            try:
                if not glob.glob("/home/pi/app/temp.jpg"):
                    shutil.copyfile(event.pathname,"/home/pi/app/temp.jpg")
                    print "created: /home/pi/app/temp.jpg"
                else:
                    print "creation of temp.jpg skipped"
            except:
                print "FAILED creation /home/pi/app/temp.jpg"
                pass
            try:
                subprocess.call(["sudo", "rm", event.pathname])
                print "Removed: "+event.pathname
            except Exception as e:
                print str(e)
                pass

def main():
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch('/home/pi/slideshow', pyinotify.ALL_EVENTS, rec=True)

    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()


