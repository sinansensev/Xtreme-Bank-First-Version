import time


def usermoneyinfo():
    usermoneydata = {"Ahmet": 0, "Zeynep": 0}
    return usermoneydata

total = usermoneyinfo()

def loginscreen():
    print("--Welcome to Xtreme Bank --")
    print("1: Login \n 2: Exit")
    loginbutton = input("Please Select Transaction ")
    while True:
        if loginbutton == "1":
            userinfodata()
            banking()

            break
        if loginbutton == "2":
            print("Exited")
            break
        else:
            loginbutton = input("The key you entered is wrong please enter a valid number")

def userinfodata():
    global username
    global usernameandpassword
    usernameandpassword = {"Ahmet": "1234", "Zeynep": "4321"}

    while True:
        username = input("Please enter a name")
        password = input("Please enter a password")
        if not username in usernameandpassword:
            print("Please try again (Name is not found)")
            continue
        if password == usernameandpassword[username]:
            print(" Welcome", username)
            break
        else:
            print("Please try again (Password is false)")
def banking():
    print("Please enter the number of the service:")
    print(" 1. Withdraw Money \n 2. Deposit Money \n 3. Transfer Money \n 4. My Account Information \n 5. Logout")
    bankingbutton = int(input(" -- "))
    while True:
        if bankingbutton == 1:
            WithdrawMoney()
            break
        if bankingbutton == 2:
            DepositMoney()
            break
        if bankingbutton == 3:
            TransferMoney()
            break
        if bankingbutton == 4:
            AccountInformation()
            break
        if bankingbutton == 5:
            Logout()
            break
        else:
            bankingbutton = int(input("Please enter valid number"))

def WithdrawMoney():
    withdraw = int(input("Please enter the amount you want to withdraw:"))
    if withdraw <= total[username]:
        total[username] = total[username] - withdraw
        print(f"{withdraw} TL withdraw from the bank. Your current balance {total[username]}. \n You are redirected back to the menu.")
        banking()
    else:
        print(f"You don't have {withdraw}TL in your account Going back to main menu...")
        banking()
def DepositMoney():
    deposit = int(input("Please enter the amount you want to drop:"))
    total[username] += deposit
    print(f"{deposit} TL deposit is completed. Your current balance {total[username]}. \n You are redirected back to the menu.")
    banking()
def TransferMoney():
    transfer = int(input("Please enter the amount you want to transfer:"))
    if transfer <= total[username]:
        total[username] -= transfer
        print(f" {transfer}TL has been transferred successuffly!\n Your current balance {total[username]}. \n Going back to main menu...")
        banking()
    else:
        print("Sorry! You don't have enough money to complete this transaction")
        print("1. Go back to main menu. \n 2. Transfer again.")
        no = int(input("--"))
        while True:
            if no == 1:
                banking()
            if no == 2:
                TransferMoney()
            break
        else:
            no = input("Please enter valid number.")
def AccountInformation():

    print(f"--- Xtreme Bank ---\n{time.asctime()}\n---")
    print(f"Your Name:{username}\nYour Password:{usernameandpassword[username]}\nYour Amount(TL): {total[username]}")
    print("Going back to main menu...")
    banking()


def Logout():
    print(f"Good Bye {username} !")


loginscreen()





