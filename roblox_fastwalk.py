import os
import colorama
import time
import threading
import socket
from colorama import Fore
from pynput.mouse import Listener as MouseListener
from pynput.mouse import Button
from pynput import keyboard
from pynput.mouse import Controller
import webbrowser

# var
title = f"""{Fore.RED}
 ▄▄▄██▀▀▀███▄    █  ███▄    █ 
   ▒██   ██ ▀█   █  ██ ▀█   █ 
   ░██  ▓██  ▀█ ██▒▓██  ▀█ ██▒
▓██▄██▓ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒
 ▓███▒  ▒██░   ▓██░▒██░   ▓██░
 ▒▓▒▒░  ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ 
 ▒ ░▒░  ░ ░░   ░ ▒░░ ░░   ░ ▒░
 ░ ░ ░     ░   ░ ░    ░   ░ ░ 
 ░   ░           ░          ░ 
{Fore.BLUE}SPEED BOOSTER{Fore.RED}\n.gg/jnn
"""
print(title)

new_script_content = """
{
    "FFlagDebugSimIntegrationStabilityTesting": "True",
    "DFIntDebugSimPhysicsSteppingMethodOverride": 10000000
}
"""

folder_path = input(Fore.GREEN+"Enter roblox client app settings folder path. For a guide type (help): ")

if folder_path == "(help)":
    webbrowser.open("https://www.youtube.com/watch?v=HqKrcHQJqJA")
    print("Help opened...")
    time.sleep(4)
    os.system("cls")
    print(title)

elif folder_path == "help":
    webbrowser.open("https://www.youtube.com/watch?v=HqKrcHQJqJA")
    print("Help opened...")
    time.sleep(4)
    os.system("cls")
    print(title)


filename_cas = os.path.join(folder_path, "ClientAppSettings.json")

confirm = input("Would you like to set fast walk? (Y/N): ").lower()

if confirm == "y" or confirm == "yes":
    with open(filename_cas, "w") as new_script_file:
        new_script_file.write(new_script_content)
        os.system("cls")
        print(title)
        print(Fore.GREEN+"Done!")
        time.sleep(3)
else:
    print(Fore.RED+"Closing program in 3 seconds..."+Fore.RESET)
    quit()

os.system("cls")
print(title)
input("Press enter to exit...")