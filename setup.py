from subprocess import STDOUT, check_call
import os

#check_call(['sudo', 'apt-get', 'update', '-y'])
#check_call(['sudo', 'apt-get', 'upgrade', '-y']) 

subprocess.call("(cd ~/temp/slideshow/)", shell=True)
