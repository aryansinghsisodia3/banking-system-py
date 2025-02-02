# Banking System

from Banking_Section_Functions import PinChange, balanceInquiry, deposit, menu, widthraw
from account_creation import getaccount_details, update_accountDetails

def login():
    chances = 3
    while chances>0:
        accountNumber = input("Enter your Account Number: ")
        entered_pin = input("Enter your Four-Digit pin: ")
        acc_details = getaccount_details(accountNumber)

        if not acc_details:
            print("Account Doesn't Exists!")
            continue

        if entered_pin != str(acc_details["pin"]):
            print("Wrong Pin")
            chances = chances-1
            print()
            if chances==0:
                print("You used all of your 3 Attempts")
                print("Your Card is now Blocked !")
                print()
                print("Please Contact Support !\n")
                break
            continue

        print("Correct Pin !")
        print()
        menu(acc_details)
        update_accountDetails(acc_details)
        break