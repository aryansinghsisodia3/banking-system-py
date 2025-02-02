from personal import (
    name_info,
    address_info,
    email_info,
    phoneNumber_info,
    pin_info,
    balance_info,
    acc_no,
)

import pickle

filename = "user_stats"


def create_account():
    NAME = name_info()
    ADDRESS = address_info()
    EMAIL_ID = email_info()
    PHONE_NUMBER = phoneNumber_info()
    PIN = pin_info()
    BALANCE = balance_info()
    ACCOUNT_NUMBER = acc_no()

    user = {
        "name": NAME,
        "address": ADDRESS,
        "email": EMAIL_ID,
        "phoneNumber": PHONE_NUMBER,
        "accountNumber": ACCOUNT_NUMBER,
        "pin": PIN,
        "balance": BALANCE,
    }

    try:
        with open(filename, "rb") as fileobj:
            users = pickle.load(fileobj)
    except:
        users = []

    users += [user] # users = users + [user]

    with open(filename, "wb") as fileobj:
        pickle.dump(users, fileobj)

    print("ACCOUNT NUMBER: ", ACCOUNT_NUMBER)
    print("PIN: ", PIN)

    print("You account has been successfully created")


def getaccount_details(acc_no):
    try:
        with open(filename, "rb") as fileobj:
            users = pickle.load(fileobj)
    except:
        users = []

    for user in users:
        if user["accountNumber"] == acc_no:
            return user
    return None

# Updates
def update_accountDetails(acc_details):

    try:
        with open(filename, "rb") as fileobj:
            users = pickle.load(fileobj)
    except:
        users = []

    for i in range(len(users)):
        if users[i]["accountNumber"] == acc_details["accountNumber"]:
            users[i] = acc_details

    with open(filename, "wb") as fileobj:
        pickle.dump(users, fileobj)


def delete_accountDetails(acc_details):
    try:
        with open(filename, "rb") as fileobj:
            users = pickle.load(fileobj)
    except:
        users = []

    users.remove(acc_details)
    del acc_details
    
    with open(filename, "wb") as fileobj:
        pickle.dump(users, fileobj)