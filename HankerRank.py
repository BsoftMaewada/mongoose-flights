# Task 
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# def weird_range(n):
#     for n in range(0, n):
#         if n > 20:
#             print(n,'Not Weird')
#         elif n % 2 == 0 and n in range(2,6):
#             print(n, 'Not Weird')
#         elif n % 2 == 0 and n in range (6, 21 ):
#             print(n, 'Weird')
#         elif n % 2 == 1:
#             print(n, 'Weird')
#         else:
#             print(n)
            
# weird_range(100)      //Works

    #SOLUTION
# import math
# import os
# import random
# import re
# import sys


# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 == 1:
#         print("Weird")
#     elif n % 2 ==0 and n in range(2,6):
#         print("Not Weird")
#     elif n % 2 == 0 and n in range(6, 21):
#         print("Weird")
#     elif n > 20:
#         print("Not Weird")

    # Task 
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example 
# a = 3
# b = 5

    #SOLUTION
# if __name__ == '__main__':
#     a = int(input()) #input a number 
#     b = int(input())

#     y = a + b
#     print(int(y))

#     x = a - b
#     print(int(x))

#     z = a * b
#     print(int(z))
 
 
    # Task
# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a // b. 
# The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.
# Example 
 

# The result of the integer division 3//5 = 0.
# The result of the float division is 3/5 = 0.6 .

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
    
#     x = a // b
#     print(x)
    
#     y = a / b
#     print(y)

    # Task 
# The provided code stub reads and integer, n , from STDIN. 
# For all non-negative integers i < n, print i^2.
# Example 
# n = 3
# The list of non-negative integers that are less than n = 3 is 0,1,2. 
# Print the square of each number on a separate line.

    #SOLUTION
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(0,n):
#         i = i ** 2 # i** 2 => i^2
#         print(i)
        
#EXERCISE

# class Account:
#     def __init__(self, acc_owner):
#         self.balance = 0
#         self.owner = acc_owner
#     def deposite(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('insufficient funds') 
#         self.balance -= amount
#             print(self.balance)
    
# class CheckingAccount(Account):
#         withdraw_charge = 1
#         def withdraw(self, amount):
#             return Account.withdraw(self, amount + self.withdraw_charge)

# class SavingsAccount(Account):
#         deposit_charge = 2
#         def deposit(self, amount):
#             return Account.deposit(self, amount - self.deposit_charge)

class Bank_Account:
    def __init__(self):
        self.balance = 0
    
        
    def deposit(self):
        amount = float(input('Enter the amount to be deposited '))
        self.balance += amount
        print('\n Amount Deposited: ', amount)
        
    def withdraw(self):
        amount = float(input('Enter the amount to withdraw '))
        if self.balance >= amount:
            self.balance -= amount
            print('\n You withdrew: ', amount)
        else:
            print('\n insufficient balance ')
            
    def display(self):
        print('\n Your Available balance: ', self.balance)
        
class SavingsAccount(Bank_Account)
        
    
        
owner = Bank_Account ()

owner.deposit()
owner.withdraw()
owner.display()


