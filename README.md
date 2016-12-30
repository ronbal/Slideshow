Preparation:<br />
Start with clean and fresh Jessy SD Image<br />
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
To prevent autostart of slidehow hit CTRL+C during start or add reset.txt to USB-Stick and boot.<br />

