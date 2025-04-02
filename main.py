from register import *
from bank import *

# Initial status of user login
status = False

print("Welcome to Akash Banking Project")
while True:
    try:
        register = int(input("1. Create an Account (Sign Up)\n"
                             "2. Log In to Your Account (Sign In)\n"
                             "Choose an option: "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input Try Again with Numbers")

# Retrieve the user's account number from the database
account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")
print(account_number[0][0])

# Banking services menu
while status:
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdrawal\n"
                             "4. Fund Transfer\n"
                             "5. Exit\n"))
        if facility >= 1 and facility <= 5:
            if facility == 1:
                bank_object = Bank(user, account_number[0][0])
                bank_object.balanceenquiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit"))
                        bank_object = Bank(user, account_number[0][0])
                        bank_object.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw"))
                        bank_object = Bank(user, account_number[0][0])
                        bank_object.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter Money to Transfer"))
                        bank_object = Bank(user, account_number[0][0])
                        bank_object.fundtransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input Number")
                        continue
            elif facility == 5:
                print("Thanks For Using Banking Services")
                status = False
        else:
            print("Please Enter Valid Input From Options")
            continue

    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue







