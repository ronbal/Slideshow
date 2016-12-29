import subprocess
from subprocess import STDOUT, check_call
import os
WorkingDir = os.getcwd()
#check_call(['sudo', 'apt-get', 'update', '-y'])
#check_call(['sudo', 'apt-get', 'upgrade', '-y'])
#check_call(['sudo', 'apt-get', 'install', 'samba', 'samba-common-bin', '-y'])
#subprocess.call("(sudo cp /home/pi/temp/bin/smb.conf /etc/samba/samba.conf)", shell=True)
#subprocess.call("(sudo /etc/init.d/samba restart)", shell=True)
subprocess.call("(sudo apt-get install python3-dev python3-setuptools libjpeg-dev zlib1g-dev libpng12-dev libfreetyp$
subprocess.call("(sudo apt-get install python3-pip)", shell=True)
subprocess.call("(sudo pip-3.2 install pi3d)", shell=True)
subprocess.call("(sudo pip-3.2 install Pillow)", shell=True)
subprocess.call("(sudo pip install pi3d)", shell=True)
subprocess.call("(sudo cp /home/pi/temp/app/shaders/*.*  /usr/local/lib/python2.7/dist-packages/pi3d/shaders)", shel$
subprocess.call("(sudo pip install pyinotify)", shell=True)

subprocess.call("(sudo mv /home/pi/temp/Advertising /home/pi/Advertising_temp)", shell=True)
subprocess.call("(sudo mv /home/pi/temp/slideshow /home/pi/slideshow_temp)", shell=True)
subprocess.call("(sudo mv /home/pi/temp/app /home/pi/app_temp)", shell=True)
