import Banking_Section_Functions
import uuid

def name_info():
    name = input("Enter your name: ")
    return name

def address_info():
    address = input("Enter your Address: ")
    return address

def email_info():
    email = input("Enter your Email-Id: ")
    return email

def phoneNumber_info():
    phoneNumber = input("Enter your Phone Number: ")
    return phoneNumber

def pin_info():
    while True:
        _pin = input("Enter the PIN you want to set: ")
        if len(_pin)<5:
            pin=_pin
            break
    return pin

def balance_info():
    balance = 0
    return balance

def acc_no():
    return str(uuid.uuid4())