import time #Time module to print date and time
kullanıcılar = {"ahmed":[1234,100],"zeynep":[4321,500],"alberto":[4422,900]} #Usernames, passwords and balance

işlem = {"ahmed":{"Withdrawals":[],"Deposits":[],"Transfers":[]},"zeynep":{"Withdrawals":[],"Deposits":[],"Transfers":[]},"alberto":{"Withdrawals":[],"Deposits":[],"Transfers":[]}}#Transaction log

admin = {"ibrahim":1122} #Admins username and password

def giris_ekranı(): #Function that prints the first screen that welcomes the user
    print ("  --- WELCOME TO ISTINYE BANK ---  \n"
           "   -------------------------------\n"
           " /           İSTANBUL             \ \n"
           f"|        {time.strftime('%D %H:%M:%S')}         | \n"
           " \                                / \n"
           "   -------------------------------\n"
    "1. Login\n"
    "2. Exit\n")
    try:
        seçim0=int(input())
        if seçim0 == 1:
            giris_ekranı2()
        elif seçim0 ==2:
            print("Exitting...")
        else: #the code that warns the user if invalid number is entered
            print("Please try again with valid numbers")
            giris_ekranı()
    except: #Try-except command that's preventing error
        print("Please try again with numbers")
        giris_ekranı()
def giris_ekranı2(): #Function that asks the user to which one to login as after choosing "Login"
    print("What do you want to login as:\n"
          "1. Admin\n"
          "2. User\n"
          "3. Go Back")
    try:
        global seçim1
        seçim1=int(input())
        if seçim1 <= 0 or seçim1 > 3: #the code that warns the user if invalid number is entered
            print("Please try again with valid numbers")
            giris_ekranı2()
        elif seçim1 == 1:
            admin_giris()
        elif seçim1 ==2:
            giris_ekranı00()
        elif seçim1 ==3:
            giris_ekranı()
    except: #Try-except command that's preventing error
        print("Please try again with numbers")
        giris_ekranı2()


def giris_ekranı00(): #Function that asks username and password
    try:
        soru2= input("Username\n")
        if soru2.lower() == "abort":
            print("Going back...")
            giris_ekranı2()
        else:
            soru3 = int(input("Password\n"))
            if soru2.lower() in kullanıcılar and soru3 == kullanıcılar[soru2][0]: #the code that checks if username and password is correct
                global kullanıcı
                kullanıcı = soru2.lower() #The variable that saves users name
                global sifre
                sifre=kullanıcılar[kullanıcı][0] #The variable that saves users password
                global bakiye
                bakiye = kullanıcılar[kullanıcı][1] #The variable that saves users balance
                ana_menu()
                return kullanıcı
                return bakiye
            else:
                print ("Username or password is wrong please try again")
                giris_ekranı00()
    except: #Try-except command that's preventing error
        print ("Please try again with numbers")
        giris_ekranı00()
def ana_menu(): #Function that asks the user which service to choose after logging in

    print(f"{kullanıcı.capitalize()} Welcome to İstinye Bank\n"
          "Please enter the number of the service\n"
    "1. Withdraw Money\n"
    "2. Deposit Money\n"
    "3. Transfer Money \n"
    "4. My Account Information\n"
    "5. Logout")
    try:
        seçim3 = int(input("\n"))
        if seçim3 <= 0 or seçim3 >= 6: #the code that warns the user if invalid number is entered
            print("Please enter a valid number")
            ana_menu()
        else:
            global bakiye
            if seçim3 == 1:
                withdraw(kullanıcı)
            elif seçim3 == 2:
                deposit()
            elif seçim3 == 3:
                transfer()
            elif seçim3 == 4:
                acc_info()
            elif seçim3 == 5:
                print("Logging out...")
                giris_ekranı2()
    except: #Try-except command that's preventing error
        print("You can only enter numbers")
        ana_menu()


def withdraw(kullanıcı): #Function that withdraws
    global bakiye
    try:
        global para_cekme
        para_cekme = int(input("Please enter the amount you want to withdraw\n"))
        if para_cekme > bakiye: #The code that checks the balance if there is enough money
            print(f"You don’t have {para_cekme} TL in your account\n"
                  "Going back to main menu...")
            ana_menu()
        elif para_cekme < 0: #The code that warns the user if negative number is entered
            print("Negative numbers cannot be entered,")
            withdraw(kullanıcı)
        else:
            print(f"{para_cekme} TL withdrawn from your account\n" #The code that prints this transaction is successful
                  "Going back to main menu...")
            bakiye -= para_cekme #The code that reduces the amonut from users balance
            işlem[kullanıcı]["Withdrawals"].append(time.strftime(f'%D %H:%M:%S {para_cekme} TL')) #The code that adds this transaction to the transaction log
            ana_menu()
    except: #Try-except command that's preventing error
        print("You can only enter numbers")
        withdraw(kullanıcı)

global bakiye
def deposit(): #Function that deposits
    global bakiye
    try:
        deposite = int(input("Please enter the amount you want to drop:\n"))
        if deposite < 0: #The code that warns the user if negative number is entered
            print("Negative numbers cannot be entered,")
            deposit()
        else:
            print(f"{deposite} TL added to your account\n" #Code that prints this transaction is successful
              "Going back to main menu...")
            bakiye += deposite #The code that adds the amount to the balance
            işlem[kullanıcı]["Deposits"].append(time.strftime(f'%D %H:%M:%S {deposite} TL')) #The code that adds this transaction to the transaction log
            ana_menu()

    except: #Try-except command that's preventing error
        print("You can only enter numbers")
        deposit()




def transfer():#Para transferi yapan fonksiyon

    transfer0 = input("Please enter the name you want to transfer to:\n")
    if transfer0.lower() == "abort":
        print("Going back to main menu...")
        ana_menu()
    elif transfer0 not in kullanıcılar or transfer0 == kullanıcı: #The code that checks the person that user wants to transfer exist
        print(f"Transfferring to user with the name {transfer0} is not possible!\n"
              f"User does not exist! "
              f"Please try again")
        transfer()
    else:
            def transfer_2(): #Function of second part of the transfer in case of any errors so it won't go to the beginnig
                global bakiye
                suanki_kullanıcı = kullanıcı
                try:
                    transfer_miktar = int(input("Please enter the amount you want to transfer\n"))
                    if transfer_miktar > bakiye: #The code that checks the balance if there is enough money to transfer
                        print("Sorry!, you don't have the entered amount\n"
                              "1. Go back to main menu\n"
                              "2. Transfer again\n")
                        try:
                            seçim = int(input())
                            while seçim < 1 or seçim > 2: #The code that warns the user if invalid number is entered
                                print("Please enter a valid number")
                                seçim = int(input("\n"))

                            if seçim == 1:
                                print("Going back to main menu...")
                                ana_menu()
                            elif seçim == 2:
                                transfer()
                        except: #Try-except command that's preventing error
                            print("You can only enter numbers, please try again")
                            transfer()

                    elif transfer_miktar < 0: #The code that warns the user if negative number is entered
                        print("Negative numbers cannot be entered")
                        transfer_2()
                    else:
                        print("Transfer successful\n" #The code that prints this transaction is successful
                              "Going back to main menu...")
                        bakiye -= transfer_miktar #The code that reduces the amonut from users balance
                        kullanıcılar[transfer0][1] += transfer_miktar #The code that adds this money to his balance
                        işlem[kullanıcı]["Transfers"].append(time.strftime(f'%D %H:%M:%S Transferred {transfer_miktar} TL to {transfer0.capitalize()} ')) #The code that adds this transaction to the transaction log
                        işlem[transfer0]["Transfers"].append(time.strftime(f'%D %H:%M:%S Transferred {transfer_miktar} TL to me from {suanki_kullanıcı.capitalize()} '))#The code that updates the persons transaction log whom this money sent to
                        ana_menu()

                except: #Try-except command that's preventing error
                    print("You can only enter numbers")
                    transfer_2()

            transfer_2()

def acc_info(): #Function that displays account information
    print(f"------İstinye Bank ------\n"
          f"------{time.strftime('%D %H:%M:%S')}------\n"
          f"------------------------------------------\n"
          f"Your Name: {kullanıcı.capitalize()}\n"
          f"Your Password: {sifre}\n"
          f"Your Balance Amount (TL): {bakiye}\n"
          f"-------------------------------------------\n"
          f"User Activity Report:\n"
          f"Your Withdrawals:\n"
          f"        {işlem[kullanıcı]['Withdrawals']}\n"
          f"Your Deposits:\n"
          f"        {işlem[kullanıcı]['Deposits']}\n"
          f"Your Transfers:\n"
          f"        {işlem[kullanıcı]['Transfers']}\n"
          f""
          f"----------------------------------------------\n"
          f"Going back to main menu...")
    ana_menu()

def admin_giris(): #Function that asks admins name and password
    try:
        adminkullanıcı = input("Username:\n")
        if adminkullanıcı.lower() == "abort":
            print("Going back...")
            giris_ekranı2()
        else:
            adminşifre = int(input("Password:\n"))
            if adminkullanıcı not in admin or adminşifre not in admin.values(): #the code that checks if username and password is correct
                print("Wrong username or password please try again")
                admin_giris()
            else:
                print(f"Welcome to the admin menu {adminkullanıcı}")
                admin_menu()

    except: #Try-except command that's preventing error
        print("You can only enter numbers")
        admin_giris()

def admin_menu(): #Function that asks to admin which service to choose after logging in
    print(f"1. Add user\n"
          f"2. Remove user\n"
          f"3. Display all users \n"
          f"4. Exit\n"
          f"Please enter the number of the service")
    try:
        seçimadmin = int(input())
        if seçimadmin <= 0 or seçimadmin >= 5: #
            print("Please try again with valid numbers") #the code that warns the user if invalid number is entered
            admin_menu()
        elif seçimadmin == 1:
            adduser()
        elif seçimadmin == 2:
            removeuser()
        elif seçimadmin == 3:
            displayaccinfo()
        elif seçimadmin == 4:
            print("Exitting...")
            giris_ekranı2()
    except: #Try-except command that's preventing error
        print("You can only enter numbers,please try again")
        admin_menu()

def adduser(): #Function that adds user
    try:
        isim= input("Please enter the users name you want to add\n")
        if isim in kullanıcılar: #Checks the name if it's already exists
            print("This user is already exist")
            adduser()
        elif isim.lower() == "abort":
            print("Going back to admin menu...")
            admin_menu()
        else:
            şifre = int(input("Please enter this users password\n"))
            kullanıcılar[isim] = [şifre,0]
            işlem[isim] = []
            print("User has been successfully added\n"
                  "Going back to admin menu...")
            admin_menu()
    except: #Try-except command that's preventing error
        print("You can only enter numbers, please try again")
        adduser()

def removeuser(): #Function that removes user
        adminseçim = input("Please enter the users name you want to remove\n")
        if adminseçim.lower() == "abort":
            print("Going back to admin menu...")
            admin_menu()

        elif adminseçim not in kullanıcılar: #Checks the name if it's exists
            print("The user you want to remove does not exist, please try again")
            removeuser()
        else:
            kullanıcılar.pop(adminseçim)
            print(f"The user {adminseçim} has been successfully removed\n"
                  f"Going back to admin menu...")
            admin_menu()


def displayaccinfo(): #Function that displays all accounts and passwords
    print("Username Password\n"
          ""
          "-------- --------")
    for i, b in kullanıcılar.items():
        print(f"{i} :   {b[0]}")
    print("-----------------------\n"
          "Going back to admin menu...")
    admin_menu()

giris_ekranı() #the code where all programme starts
