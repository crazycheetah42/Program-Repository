import time
import shutil
import os
import platform
import getpass
print("Please wait while AryamanOS initializes setup...")
pc_has_been_setup_file = open("pc_has_been_setup.txt")
pc_has_been_setup = pc_has_been_setup_file.readline()
if pc_has_been_setup == "false":
    print("Welcome to AryamanOS! This will help you setup your PC.")
    time.sleep(1)
    username = input("Who is using AryamanOS?\n")
    password = getpass.getpass(prompt=f"Enter the password for {username}:\n")
    device_name = input("What do you want to call your AryamanOS PC?\n")
    print("That's all the information we need right now. Please wait while we configure AryamanOS and set it up for you...")
    username_file = open("username.user", 'w')
    password_file = open(f"passwords.pass", 'w')
    device_name_file = open("device_name.devname", 'w')
    username_file.writelines(username)
    password_file.writelines(f"{password}")
    device_name_file.writelines(device_name)
    pc_has_been_setup_file.write("true")
    print("We have installed, configured, and set up AryamanOS for you.\nWe will reboot in 5 seconds...")
    time.sleep(1)
    print("We will reboot in 4 seconds...")
    time.sleep(1)
    print("We will reboot in 3 seconds...")
    time.sleep(1)
    print("We will reboot in 2 seconds...")
    time.sleep(1)
    print("We will reboot in 1 second...")
    time.sleep(1)
    if platform.system() == "Linux" or platform.system() == "Mac":
        os.system("clear && python3 aryamanOS.py")
    if platform.system() == "Windows":
        os.system("cls && python aryamanOS.py")
elif pc_has_been_setup == "true":
    print("Error: Your AryamanOS PC has already been setup.")
    if platform.system() == "Linux" or platform.system() == "Mac":
        os.system("clear && python3 aryamanOS.py")
    if platform.system() == "Windows":
        os.system("cls && python aryamanOS.py")