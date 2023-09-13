import random
import os
import subprocess
from webbrowser import get

def get_rand():
    return random.choice("abcdef0123456789")

def new_mac():
    new = ""
    for i in range(0,5):
        new += get_rand() + ":"

    new += get_rand() + get_rand()
    return new

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

# Turn off Ethernet 0 Interface
subprocess.call(["sudo","ifconfig","eth0","down"])

new_m = new_mac()

# Specify MAC Address and Turn on Ethernet 0 Interface
subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m])
subprocess.call(["sudo","ifconfig","eth0","up"])

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))