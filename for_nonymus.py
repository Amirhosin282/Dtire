import sys
from rainbowtext import text
from pyfiglet import *
import pyfiglet
from time import sleep

target = "amirhosin282"
guess = ''
for index, character in enumerate(target): # this code for loding animaition
    j = ord(' ')
    while True:
        sys.stdout.write(f'\r{text(figlet_format(guess, font="slant"))}{text(figlet_format(chr(j), font="slant"))}')
        os.system("cls")
        sys.stdout.flush()
        sleep(0.00001)
        if chr(j) == character:
            guess += character
            break
        j += 1
