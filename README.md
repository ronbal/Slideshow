Preparation:<br />
Start with clean, fresh and updated Raspbian SD Image<br />
https://www.raspberrypi.org/downloads/raspbian/<br />
<br />
<br />
In Desktop Enviorenment:<br />
Startx: Menu -> Preferences -> System -> Boot: To CLI<br />
Performance -> GPU Memory: 128<br />
Then reboot<br />
<br />
<strong>Disconnect any USB-Drives bevor executing the setup command</strong><br />
Copy commands to CLI without ->"<-<br />
"sudo git clone https://github.com/Hatschi915/Slideshow.git /home/pi/temp"<br />
"cd temp"<br />
"sudo python setup.py"<br />
<br />
<br />
Wait for reboot then connect USB-Stick<br />
To prevent autostart add reset.txt to USB-Stick and boot.<br />
<br />
<strong>Featuers:</strong><br />
Preconfigured samba share, to access all needed folders and settings<br />
New pictures shown first, then randomly<br />
Display advertisment after x pictures<br />
<br />
<strong>Need to know:</strong><br />
To prevent autostart add a reset.txt file to the USB-Stick and boot.<br />
<br />
Samba share structure:<br />
Advertising: Folder for Ads<br />
Application: The scripts and setting.ini file<br />
Slideshow Hotfolder: Here you put new files in<br />
USB Stick: The content of the slideshow<br />
<br />
Behaviour:<br />
The Slideshow works with an attached USB stick<br />
Any new .jpg/JPG/jpeg/JPEG file putted into the slideshow hotfolder will be displayed first and<br />
then moved to the USB Stick. If there is no file on the USB Stick the slideshow will display the ads<br />
If there is content on the USB Stick the slideshow will show it´s content in random order and after x pictures a ad.<br />
If the is no USB Stick attached new pictures will be displayed but deleted after.<br />
The USB Stick can be disconnected and reconnected while the slideshow is running<br />
<br />
PLEASE READ LICENSING AND COPYRIGHT NOTICES ESPECIALLY IF USING FOR COMMERCIAL PURPOSES<br />

