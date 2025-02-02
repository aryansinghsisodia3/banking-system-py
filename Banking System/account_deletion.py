import pickle
from account_creation import delete_accountDetails, getaccount_details

filename = "user_stats"


def delete_account():
    accountNumber = input("Enter your Account Number: ")
    entered_pin = input("Enter your Four-Digit pin: ")
    acc_details = getaccount_details(accountNumber)

    if not acc_details:
        print("Account Doesn't Exists!")
        return

    if entered_pin != str(acc_details["pin"]):
        print("Wrong Pin")
        return

    print("Correct Pin !")
    delete_accountDetails(acc_details)



    print()