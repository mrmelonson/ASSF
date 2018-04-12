import time

def Greenprint(words):
    print("\033[31;1;4mHello\033[0m")

def PrintTitle():
    print("    _                   _ _                              __                _   ")
    print("   /_\    ____ __  __ _| | |  ____ _  _____ __ ___  _   / _|___ _ _ ___ __| |_ ")
    print("  / _ \  (_-< '  \/ _` | | | (_-< ' \/ _ \ V  V / || | |  _/ _ \ '_/ -_|_-<  _|")
    print(" /_/ \_\ /__/_|_|_\__,_|_|_| /__/_||_\___/\_/\_/ \_, | |_| \___/_| \___/__/\__|")
    print("                                                 |__/                          ")

def Print(words):
    time.sleep(0.5)
    print(">" + words)