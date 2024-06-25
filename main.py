from art import logo
print(logo)

import os

def calculator():
    user_choice = 'yes'
    while(user_choice == 'yes'):
        num1 = int(input("Enter the first number: "))
        operation = input("Enter the operation you want to perform- '+', '-', '*', '/': ")
        num2 = int(input("Enter the second number: "))
        
        if operation == "+":
            ans = num1 + num2
        elif operation == "-":
            ans =  num1 - num2
        elif operation == "*":
            ans =  num1 * num2
        elif operation == "/":
            ans =  num1 / num2
        else:
            return ("Enter a valid operation")
        print(f"{num1} {operation} {num2} = {ans}")
        user_choice = input("Enter 'yes' if you want to continue or 'no' if you want to exit.").lower()
        os.system('cls')
        print(logo)
        
print(calculator())