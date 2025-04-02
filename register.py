# Registration & Authentication System for Banking Application
from database import *
from customer import *
from bank import Bank
import random

def SignUp():
    username = input("Enter a Unique Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("This username already exists. Please choose another.")
        SignUp()
    else:
        print("Username is available. Let's proceed!")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your new account number is: {account_number}", account_number)
                break
    customer_object = Customer(username, password, name, age, city, account_number)
    customer_object.createuser()

    bank_object = Bank(username, account_number)
    bank_object.create_transaction_table()


def SignIn():
    username = input("Enter Your Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome Back, {username.capitalize()}! Please Enter Enter Password: ")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("You have successfully Signed IN!")
                return username
            else:
                print("Incorrect Password. Please Try Again")
                continue
    else:
        print("No account found with this username. Please check and try again.")
        SignIn()
