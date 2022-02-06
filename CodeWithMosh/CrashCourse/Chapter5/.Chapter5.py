#-------- IF STTEMENTS ---------#
cars = ['audi', 'bmw', 'subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
#INEQUALITY

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')
    
#NUMBER COMPARISONS
answer = 17

if answer != 42:
    print("That is not the correct answer, please try again!")
    
#Checking weather a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
print(requested_toppings)

'pepperoni' in requested_toppings 
print(requested_toppings)

#Checking weather a value is NOT in a list
banned_users = ['andrew', 'carolina','david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
#SIMPLE IF STTEMENTS
age = 19
if age >= 18:
    print("You are old enough to vote!")
    ## add
    print("Have you registered to vote yet?")
    
#IF - ELSE STTEMENTS

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18.")

#THE IF - ELIF - ELSE

# age = int(input("Enter age: "))

# if age < 4:
#     print("You can enter for FREE.")
# elif age < 18:
#     print("Your ticket price is $25.")
# else:
#     print("Your ticket price is $40.")

#better way

# age = int(input("Enter an age:"))

# if age < 4:
#     price = 0.00
# elif age < 18:
#     price = 25.00
# else:
#     price = 45.00
# print(f"Your admission cost is ${price}")

# #it’s important to check all of the conditions of interest. 
# # In this case, you should use a series of simple if statements 
# # with no elif or else blocks.

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding Pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinish making your pizza!")

# #Using if Statements with Lists
# requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']

# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")

# print("\nFinish making your pizza!")

# #But what if the pizzeria runs out of green peppers? An if statement
# #inside the for loop can handle this situation appropriately:

# for requested_topping in requested_toppings:
#     if requested_topping == "green pepper":
#         print(f"Sorry we dont have {requested_topping} right now.")
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza")

#Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green pepper', 'pepperoni', 'extra cheese']

requested_toppings = ['mushrooms','french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we dont have {requested_topping}")
        
print("\nFinish making your pizza!")