# Banking System Functions


def menu(acc_details):

    while True:
        print("""
        ┎----------------------┒
        |   BANKING SECTION -  |
        ┖----------------------┛
        """)


        print(' => PRESS 1 FOR BALANCE INQUIRY')
        print(' => PRESS 2 FOR WIDTHDRAWL')
        print(' => PRESS 3 FOR DEPOSIT')
        print(' => PRESS 4 FOR PIN CHANGE')
        print(' => PRESS 5 FOR LOGOUT')
        print()

        option = int(input('Enter your option: '))
        print()

        # Balance Enquiry
        if option == 1:
            balanceInquiry(acc_details)

        # Widthrawl
        elif option == 2:
            widthraw(acc_details)

        # Deposit
        elif option == 3:
            deposit(acc_details)

        # New Pin
        elif option == 4:
            PinChange(acc_details)

        # Logout
        elif option == 5:
            break

        
        # if option !=[1,2,3,4] ... then, Invalid Option will be printed
        else:
            print('Invalid Option')
        
        restart = input("Would you like to continue?")
        if restart in ('n', 'no', 'NO', 'n'):
            print('Thank You For Banking With ICICI Bank')
            break


def balanceInquiry(acc_details):
    print('Your Current Balance is $', acc_details["balance"])


def widthraw(acc_details):
    if acc_details["balance"]>0:
        widthrawl = int(input('What would you like to widthraw? \n $10/$20/$50/$100/$500: '))
        if widthrawl in [10,20,50,100,500]:
            if acc_details["balance"] > widthrawl:
                acc_details["balance"] = acc_details["balance"]-widthrawl
                print('Your New Balance is $', acc_details["balance"])
            else:
                print("Insufficient Balance")
        elif widthrawl!=[10,20,50,100,500]:
            print('Invalid Amount')

    elif acc_details["balance"] <= 0:
        print("You are Broke")
        print("Your Balance is 0$")
        print()


def deposit(acc_details):
    deposit_money = int(input('Enter the Amount You Want to Deposit: '))
    acc_details["balance"] = deposit_money+acc_details["balance"]
    print('Your New Balance is $', acc_details["balance"])


def PinChange(acc_details):
    n_pin = input('Enter New Pin: ')
    acc_details["pin"] = n_pin                          # changed pin to acc_details["pin"]
    print('Your New Pin is', acc_details["pin"])