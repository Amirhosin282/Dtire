# this is func and pips
# this file imported on main file(Dtire.py)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from time import sleep
from khayyam import JalaliDate
from colorama import Fore
import sys
import os
import random
from pyfiglet import figlet_format
from rainbowtext import text
import requests
import platform

def cl():
    if platform.system() == 'Linux':
        return 'clear'
    elif platform.system() == 'Windows':
        return 'cls'

# var's
date_time = JalaliDate.today() # jalali date
#

if __name__ == '__main__': # sey to user
    os.system(cl())
    print(Fore.RED, 'run Dtire.py, this is not main file ')
    sleep(5)
    sys.exit()


# funcs

# def ReadingData(): # for reading data
#     f = open("data/data.txt", "r")
#     print(Fore.WHITE)
#     print(f.read())
#     f.close()
#

def InstallPip(): # installing pip
    os.system("pip install khayyam")
    os.system("pip install selenium")
    os.system("pip install time")
    os.system("pip install colorama")
    os.system("pip install sys")
    os.system("pip install tqdm")



def loading(a): # loading view
    for i in tqdm (range (100), 
               desc="Loading ...", 
               ascii=False, ncols=75):
        sleep(a)





rd, gn, lgn, yw, lrd, be, pe, cn = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m', '\033[00;36m'



def view(a): # app banner
    
    os.system(cl())

    print(Fore.GREEN)
    print(a)

    print(Fore.BLUE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")

    print(Fore.RED, "sabte name tier dolati (kavir)")

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")

    print(Fore.RED,'    time',Fore.GREEN, a)
    print(Fore.RED,'    email',Fore.GREEN,' amirhosinasdpwr@gmail.com')

    print(Fore.RED,'    by',Fore.BLUE,' amirhosin282')
    print(Fore.WHITE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")
    
 
def exit(a, b): # a func for giving exit from user
    sleep(a)
    print(Fore.RED, "good bye")
    sleep(b)
    sys.exit()
    
    

def numb(a):
    file = open(a, "+r")
    numb = str(file.read())
    file.close()
    return numb


def ChengNumb(a, b):
    os.remove(a)
    file = open(a, "a+")
    file.write(str(int(b) + 1))
    file.close()

#
