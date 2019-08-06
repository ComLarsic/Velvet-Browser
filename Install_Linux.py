#!/usr/bin/python3.6
import os
import getpass


usr = input("Type the current username of the linux user: ")
dir = os.path.dirname(os.path.abspath(__file__))

os.system("sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0")
os.system(f"mkdir /home/{usr}/Velvet/")
os.system(f"touch /home/{usr}/Velvet/history.txt")
os.system(f"sudo touch /usr/share/applications/Velvet.desktop")
os.system(f"cp -a {dir}/. /home/{usr}/Velvet")
with open(f"/usr/share/applications/Velvet.desktop", 'a') as desk:
     desk.write(f"[Desktop Entry]\nVersion=1.0\nExec=/home/{usr}/Velvet/main.py\nName=Velvet\nGenericName=Velvet\nComment=Connect to The Internet\nEncoding=UTF-8\nTerminal=true\nType=Application\nCategories=Application;Network;")
