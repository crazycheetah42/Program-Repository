import os
import shutil
import getpass
import platform
print("Starting AryamanOS...")
pc_has_been_setup_file = open("pc_has_been_setup.txt", 'r', encoding='utf8')
pc_has_been_setup = pc_has_been_setup_file.readline()
def aryamanOS():
    cwd = os.getcwd()
    command, command_parameters = input(f'{current_user}@{hostname}:{cwd}$ ').split()
    if "mkdir" in command:
        os.mkdir(command_parameters)
        aryamanOS()
    if "rmdir" in command:
        os.rmdir(command_parameters)
        aryamanOS()
    if "cp" in command:
        shutil.copy(command_parameters)
        aryamanOS()
    if "mv" in command:
        shutil.move(command_parameters)
        aryamanOS()
    if "help" in command:
        help_file = open(f"{command_parameters}.hlp", 'r')
        program_help = help_file.readline()
        aryamanOS()
    if "touch" in command:
        open(command_parameters, 'x')
        aryamanOS()
    if "list" in command:
        commands = ['help', 'mv', 'cp', 'rmdir', 'mkdir', 'touch', 'cd', 'python3']
        print(commands)
        print("DO NOT ENTER MORE THAN 1 PARAMETER TO ANY COMMAND. Type 'help command_name' to get help on a command and how to use it.")
        aryamanOS()
    if "cd" in command:
        os.chdir(command_parameters)
        aryamanOS()
    if "python3" in command:
        if platform.system() == "Linux" or platform.system() == "Mac":
            os.system(f"python3 {command_parameters}")
            aryamanOS()
if pc_has_been_setup == "false":
    import oobe
else:
    desktop_name_file = open("device_name.devname", 'r', encoding="utf8")
    hostname = desktop_name_file.readline()
    current_user = ""
    print(f"Enter the username for {hostname}.")
    print("Select a user from the list of users:")
    username_file = open("usernames.user")
    usernames = username_file.readlines()
    print(usernames)
    username_input = input()
    if username_input in usernames:
        current_user = username_input
        password_file = open("passwords.pass", 'r', encoding="utf8")
        passwords = password_file.readlines()
        password_input = getpass.getpass(prompt=f"Enter the password for {username_input}:\n")
        if password_input in passwords:
            print(f"Preparing AryamanOS for you, {username_input}")
            cwd = os.getcwd()
            aryamanOS()
    elif username_input not in usernames:
        print("Username not found, please try again.")
        if username_input in usernames:
            current_user = username_input
            print(f"Enter the password for {username_input}:")
            password_file = open("passwords.pass", 'r', encoding="utf8")
            passwords = password_file.readlines()
            password_input = input()
            if password_input in passwords:
                print(f"Preparing AryamanOS for you, {username_input}")
                cwd = os.getcwd()
                print("Important note: If you want help, type help with the command name you want. e.g 'help mv'. If you want a list of commands, type 'list commands'.")
                aryamanOS()