#!/usr/bin/python3.6
import os

usr = input("Type the current username of the linux user: ")

os.system("rm /usr/share/applications/Velvet.desktop")
os.system(f"rm -rf /home/{usr}/Velvet/")
os.system(f"echo Done!")