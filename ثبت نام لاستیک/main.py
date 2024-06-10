import os
try:
    from requests import post, get
    from khayyam import JalaliDate
    from time import sleep
    from pyfiglet import figlet_format
    from rainbowtext import text
    from colorama import Fore
    import requests
    import datetime
    import sys
except:
	os.system("python3 -m pip install -r more/pip.txt")


data = open("Data/data.txt", "+a")

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
os.system("cls")


date = JalaliDate.today()



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
        
        
print(Fore.GREEN)
print(date)

print(Fore.BLUE)


print(text(figlet_format("amirhosin282", font="slant")))

print(Fore.YELLOW)
print("_________________________________________________________________                                                                                             ")

print(Fore.RED,'    time',Fore.GREEN, date)
print(Fore.RED,'    email',Fore.GREEN,' amirhosinasdpwr@gmail.com')

print(Fore.RED,'    by',Fore.BLUE,' amirhosin282')
print(Fore.WHITE)

print(Fore.YELLOW)
print("_________________________________________________________________                                                                                             ")

print(Fore.CYAN)





# start code

name = input("your name: ").strip() # giving informatition from user (name)

code_m = input("code e meli: ").strip() # giving informatition from user (national code)

sbs = input("shomare e barge e sabz: ").strip() # giving informatition from user (green card number)

t_size = input("size (13 - 14 - 15): ").strip() # giving informatition from user (tier size)

phone_number = input("phone number: ").strip() # giving informatition from user (phoone number)

tedada_t = input("tedad taier (1 - 2 - 3 - 4): ").strip() # giving informatition from user (number of tiers)






user = "\n name:  " + name + "\n national code:  " + code_m + "\n green card number:  " + sbs + "\n tire size:  " + t_size + "\n phone number:  " + phone_number \
    + "\n numb of tire:  " + tedada_t + "\n" +"time:  "  + str(date) + "\n \n" # this is user informatition
    

send_req = None

try: # saving data to Data/data.txt
    data.write(user)
except:
    print(Fore.RED, "saving error")
    send_req = False
    




url = "https://kala.ntsw.ir" # url site


send = { # site filds id
    "NationalCodeField": code_m,
    "NoteNumberField": sbs,
    "SizeField": t_size,
    "MobileNoField": phone_number,
    "TireCountField":tedada_t
}


        
data.close() # closing data file


while send_req is not False: # sending request
    try:
        req = requests.post(url, send, "TireSedan")
        if req.status_code == 200:
            print(Fore.GREEN, " successful  ", req.status_code)
        elif req.status_code == 404:
            print(Fore.RED, "   404 error  ", req.status_code)
    except:
        print(Fore.RED, "connection error")
        
    sleep(1)
else:
    print(Fore.RED, "error")