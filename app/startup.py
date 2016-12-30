import socket 
import fcntl 
import struct 
import subprocess
import time
import sys
import os
from subprocess import check_output
import glob
import select

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
    
    
config = ConfigParser()
config.read('/home/pi/app/settings.ini')
USB_only_mode = config.getboolean('startup_setting', 'USB_only_mode')

subprocess.call("clear", shell=True)
try:
    for i in xrange(10,0,-1):        
        print ("*** Starting Slideshow ***")
        #print ("Hit CTRL+C in 10 Seconds to prevent startup")
        print (i)
        time.sleep(1)
        subprocess.call("clear", shell=True)
    if not glob.glob("/media/usb/reset.txt"):
        if not USB_only_mode:
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
except KeyboardInterrupt:
    print ("")
    print ("STARTUP ABORTED")
    sys.exit(0)
