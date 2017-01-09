import socket 
import fcntl 
import struct 
import subprocess
import time
import sys
import os
from subprocess import check_output
import glob
import time
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
    
    
config = ConfigParser()
config.read('/home/pi/app/settings.ini')
Skip_IP_Check = config.getboolean('startup_setting', 'Skip_IP_Check')
Expand_image = config.getboolean('slideshow_settings', 'Expand_image')

if Expand_image:
    subprocess.call("sudo cp /usr/local/lib/python2.7/dist-packages/pi3d/shaders/shaders/blend_include_fs1.inc /usr/local/lib/python2.7/dist-packages/pi3d/shaders/shaders/blend_include_fs.inc", shell=True)
else:
    subprocess.call("sudo cp /usr/local/lib/python2.7/dist-packages/pi3d/shaders/shaders/blend_include_fs2.inc /usr/local/lib/python2.7/dist-packages/pi3d/shaders/shaders/blend_include_fs.inc", shell=True)




                
if not glob.glob("/media/usb/reset.txt"):
    if not Skip_IP_Check:
        ips = check_output(['hostname', '--all-ip-addresses'])
        if ips.strip():
            print "got ip"
            print ips
            subprocess.call("sudo python /home/pi/app/Hotfolder.py &", shell=True)
            subprocess.call("sudo python /home/pi/app/Slideshow.py &", shell=True)
            sys.exit(0)                
        else:
            print "NO IP"
            sys.exit(0)
    else:
        subprocess.call("sudo python /home/pi/app/Hotfolder.py &", shell=True)
        subprocess.call("sudo python /home/pi/app/Slideshow.py &", shell=True)
        print ("USB ONLY MODE")
        sys.exit(0)
else:
    print ("\x1b[0;31;40m"+"RESET.txt detected. Skipping Autostart"+"\x1b[0;37;40m")
    os.remove("/media/usb/reset.txt")
    sys.exit(0)
