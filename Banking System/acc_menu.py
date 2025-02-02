from account_creation import create_account
from account_deletion import delete_account
from Banking_Section import login
from support import support_section

print("Welcome to Supreme Banking")


def acc_menu():
   while True:
      print("""
┎---------------------------------┒
|   ACCOUNT MANAGEMENT SECTION -  |
┖---------------------------------┛
""")
      print(" => PRESS 1 FOR CREATING NEW ACCOUNT")
      print(" => PRESS 2 DELETING YOUR EXISTING ACCOUNT")
      print(" => PRESS 3 FOR LOGGING INTO AN EXISTING ACCOUNT")
      print(" => PRESS 4 FOR HELP")
      print(" => PRESS 5 FOR EXIT")
      print()

      option = int(input("Enter your option: "))
      print()

      # CREATE ACCOUNT
      if option == 1:
         create_account()

      # DELETE ACCOUNT
      elif option == 2:
         delete_account()

      # LOGIN
      elif option == 3:
         login()

      # HELP
      elif option == 4:
         support_section()

      # Exit
      elif option == 5:
         break

      # if option !=[1,2,3,4] ... then, Invalid Option will be printed
      else:
         print("Invalid Option")
         restart = input("Would like to go back to Menu ? ")
         if restart in ("n", "no", "NO", "n"):
            print("Thank You For Banking With Supreme Bank")
            break

acc_menu()