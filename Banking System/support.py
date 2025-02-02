def support_section():
    print(
        """
    ┎----------------------┒
    |   SUPPORT SECTION -  |
    ┖----------------------┛

    Most commonly asked questions are listed below -


    (1)  => Q: How to Create a new Account?
    (2)  => Q: How to Delete an Existing Account?
    (3)  => Q: How to Login into an existing Account?
    (4)  => Q: How to Edit Details for Personal Info Section?
    (5)  => Q: How to use the Account Management Section?
    (6)  => Q: How can they unblock their card?

    Still not answered?
    Conctact > [+91 1000-68-1200]

    Enter the corresponding number to ask the Question.
    [ 1 / 2 / 3 / 4 / 5 / 6 / 7 ]
    """
    )

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        print("To create a new Account you need -")
        print()
        print("Name, Address, Email-Id, Phone Number")
        print("When you enter all these details you would be given an Account Number(32 chrs)")
        print("Which will be used in terms of logging in, and you need to memorize the")
        print("Account Number as well as the PIN you chose to be associated with it.")
        print()
        print("Ex- Account Number - xx0xx1xx-x95x-x0xx-x71x-xxxcxxxxbxxx ")
        restart = input('Would like to go back to Menu ? ')
        if restart not in ('n', 'no', 'NO', 'N'):
            support_section()
        if restart in ('n', 'no', 'NO', 'N'):
            print('Thank You For Banking With Supreme Bank')
            exit()

    elif choice == 2:
        print("To delete an existing Account -")
        print()
        print("You need to verify your account number with PIN")
        print("And you account would be deleted.")
        restart = input('Would like to go back to Menu ? ')
        if restart not in ('n', 'no', 'NO', 'n'):
            support_section()
        if restart in ('n', 'no', 'NO', 'n'):
            print('Thank You For Banking With Supreme Bank')
            exit()

    elif choice == 3:
        print("To Login into an existing Account -")
        print()
        print("You need to verify your account number with PIN")
        print("And you would be Logged in for Banking Transactions.")
        restart = input('Would like to go back to Menu ? ')
        if restart not in ('n', 'no', 'NO', 'n'):
            support_section()
        if restart in ('n', 'no', 'NO', 'n'):
            print('Thank You For Banking With Supreme Bank')
            exit()

    elif choice == 4:
        print()

    elif choice == 5:
        print(" On Account Management section you will see following options")
        print()
        print(" => PRESS 1 FOR CREATING NEW ACCOUNT --- this option is used for creating account")
        print(" => PRESS 2 DELETING --- this option is used for deleting account")
        print(" => PRESS 3 FOR LOGGING INTO AN EXISTING ACCOUNT --- this option is used for Logging In")
        print(" => PRESS 4 FOR EXIT")
        restart = input('Would like to go back to Menu ? ')
        if restart not in ('n', 'no', 'NO', 'n'):
            support_section()
        if restart in ('n', 'no', 'NO', 'n'):
            print('Thank You For Banking With Supreme Bank')
            exit()

    elif choice == 6:
        print("For unblocking of your card")
        print("Call on +91 1000-68-1201")
        restart = input('Would like to go back to Menu ? ')
        if restart not in ('n', 'no', 'NO', 'n'):
            support_section()
        if restart in ('n', 'no', 'NO', 'n'):
            print('Thank You For Banking With Supreme Bank')
            exit()