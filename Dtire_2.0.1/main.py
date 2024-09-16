import os
try:
    from khayyam import JalaliDate
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep
    from pyfiglet import *
    import pyfiglet
    from rainbowtext import text
    from colorama import Fore
    import datetime
    import sys
except:
        os.system("pip install khayyam")
        os.system("pip install selenium")
        os.system("pip install time")
        os.system("pip install pyfiglet")
        os.system("pip install rainbowtext")
        os.system("pip install colorama")
        os.system("pip install sys")

try:
    data = open("Data/data.txt", "+a")
except:
    print(Fore.RED, "opening error")

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'


# info
print(data)
sleep(0.8)
os.system("cls")
print("if you have error lern tuturial or send me on email")
print("amirhosinasdpwr@gmail.com")
print("by amirhosin282")
print("v : 2.01")
print("lodaing ... ")
sleep(5)
os.system("cls")
#

#spansers
print(pyfiglet.figlet_format('sepehr', font = 'isometric1'))
sleep(5)
#

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



sleep(1)
os.system("cls")       
        
print(Fore.GREEN)
print(date); print("2.01")


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






user = "\n name:  " + name + "\n national code:  " + code_m + "\n green card number:  " + sbs + "\n tire size:  " +\
       t_size + "\n phone number:  " + phone_number+ "\n numb of tire:  " + tedada_t + "\n" +"time:  "  + str(date) + \
       "\n \n" # this is user informatition
    

send_req = None

try: # saving data to Data/data.txt
    data.write(user)
except:
    print(Fore.RED, "saving error")
    send_req = False
    




url = "https://kala.ntsw.ir" # url site


      
data.close() # closing data file



driver = webdriver.Firefox() # find driver

driver.get(url)



try: # skip buttons
    sleep(2) # skiping button1
    b1 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "tirebox"))
    )
    b1.click()#
    
    sleep(2) # skiping button2
    b2 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-danger"]'))
    )
    b2.click()#
    
except:
    print(Fore.RED, "selection error")
    
    
    
try: # send info
    _input1 = driver.find_element(By.ID, "NationalCodeField")
    _input1.send_keys(code_m) # giveing to api national code
    
    sleep(1)
    _input2 = driver.find_element(By.ID, "NoteNumberField")
    _input2.send_keys(sbs) # giving to api green card number
    
    sleep(1)
    _input3 = driver.find_element(By.ID, "SizeField")
    _input3.send_keys(t_size) # giving to api tier size
    
    sleep(1)
    _input4 = driver.find_element(By.ID, "MobileNoField")
    _input4.send_keys(phone_number) # giving to api phone number
    
    sleep(1)
    _input5 = driver.find_element(By.ID, "TireCountField")
    _input5.send_keys(tedada_t) # giveing to api numb of tier
    
    send_req = True
except:
    print(Fore.RED, "info error")
    send_req = False
    
    

try: # login button
    print(Fore.GREEN, "  print cabtcha code in website")
    sleep(15)
    send = driver.find_element(By.ID, "TireSedan")
    send.click()
except:
    print(Fore.RED, "login error")




# giving tier

# TODO