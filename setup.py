import subprocess
from subprocess import STDOUT, check_call
import os
WorkingDir = os.getcwd()
check_call(['sudo', 'apt-get', 'update', '-y'])
#check_call(['sudo', 'apt-get', 'upgrade', '-y'])
check_call(['sudo', 'apt-get', 'install', 'samba', 'samba-common-bin', '-y'])
check_call(['sudo', 'apt-get', 'install', 'usbmount', '-y'])
subprocess.call("(sudo cp /home/pi/temp/bin/smb.conf /etc/samba/smb.conf)", shell=True)
check_call(['sudo', 'apt-get', 'install', 'python3-dev', 'python3-setuptools', 'libjpeg-dev', 'zlib1g-dev', 'libpng12-dev', 'libfreetype6-dev', '-y'])
check_call(['sudo', 'apt-get', 'install', 'python3-pip', '-y'])
check_call(['sudo', 'apt-get', 'install', 'apache2', '-y'])
check_call(['sudo', 'apt-get', 'install', 'php5', 'libapache2-mod-php5', '-y'])
subprocess.call("(sudo pip-3.2 install pi3d)", shell=True)
subprocess.call("(sudo pip-3.2 install Pillow)", shell=True)
subprocess.call("(sudo pip install pi3d)", shell=True)
subprocess.call("(sudo mkdir /usr/local/lib/python2.7/dist-packages/pi3d/shaders/shaders)", shell=True)
subprocess.call("(sudo cp /home/pi/temp/app/shaders/*.*  /usr/local/lib/python2.7/dist-packages/pi3d/shaders/shaders)", shell=True)
subprocess.call("(sudo pip install pyinotify)", shell=True)
subprocess.call("(sudo mkdir /home/pi/advertising)", shell=True)
subprocess.call("(sudo cp -r /home/pi/temp/Advertising/*.* /home/pi/advertising)", shell=True)
subprocess.call("(sudo mkdir /home/pi/slideshow)", shell=True)
subprocess.call("(sudo mkdir /home/pi/app)", shell=True)
subprocess.call("(sudo cp -r /home/pi/temp/app/*.* /home/pi/app)", shell=True)
subprocess.call("(sudo mkdir /home/pi/void)", shell=True)
subprocess.call("(sudo cp -r /home/pi/temp/void/*.* /home/pi/void)", shell=True)
subprocess.call("(sudo cp /home/pi/temp/bin/rc.local /etc/rc.local)", shell=True)
subprocess.call("(sudo cp /home/pi/temp/bin/usbmount.conf /etc/usbmount/usbmount.conf)", shell=True)
subprocess.call("(sudo cp -r /home/pi/temp/bin/server/*.* /var/www/html)", shell=True)
subprocess.call("(sudo rm /var/www/html/index.html)", shell=True)
subprocess.call("(sudo cp /home/pi/temp/bin/index.php /var/www/html/index.php)", shell=True)
subprocess.call("(sudo cp /home/pi/temp/bin/.donotdelete.txt /media/usb/.donotdelete.txt)", shell=True)
proc = subprocess.Popen(['sudo', 'smbpasswd', '-a', 'pi'], stdin=subprocess.PIPE)
proc.communicate('raspberry\nraspberry\n')
subprocess.call("(sudo chown -R pi:pi /home/pi/app)", shell=True)
subprocess.call("(sudo chown -R pi:pi /home/pi/advertising)", shell=True)
subprocess.call("(sudo chown -R pi:pi /home/pi/slideshow)", shell=True)
subprocess.call("(sudo chown -R pi:pi /var/www)", shell=True)
subprocess.call("(sudo chown -R www-data:www-data /home/pi/app/settings.ini)", shell=True)
subprocess.call("(sudo chmod +x /etc/rc.local)", shell=True)
subprocess.call("(sudo reboot)", shell=True)
