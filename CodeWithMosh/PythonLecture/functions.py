# Defining Functions
def greet():
    print('Hi there')
    print('Welcome aboard')
    
greet()

# Arguments
def greet(first_name, last_name):
    print(f'{first_name} {last_name}')
    
greet('Buhari', 'Maiwada')

# Types of Functions
def greet(name):
    print('Hi', name)

# 1 - Perform a tasks
# 2 - Return a value

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting('Buhari')
print(message)

# file = open('content.txt', 'w') #working with file
# file.write(message)

def greet(name):
    print(f"Hi {name}")
    
print(greet("Buhari"))

# Keyword Arguments
def increment(number, by):
    return number + by
# result = increment(2, 1)
# print(result)

print(increment(2, by=1)) #by=1 is a keyword argument

# Default Arguments
def increment(number, by=1): # by=1 is a default argument
    return number + by
print(increment(2, 5))

# *args
def multiply(x,y):
    return x * y

multiply(2, 3)

def multiply(*numbers):
    print(numbers)
    # iterate
    for number in numbers:
        print(number)
    
multiply(2, 3, 4, 5)

# to calculate and print of the products of numbers
def multiply(*numbers):
    total = 1
    # iterate
    for number in numbers:
        total *= number
    return total
    
print(multiply(2, 3, 4, 5))

# **args = passing multiply keyword arguments
def save_user(**user):
    print(user)
    
save_user(id=1, name= 'Buhari', age='36')


def save_user(**user):
    # passing the key value
    print(user['id'])
    
save_user(id=1, name='Buhari', age='36')

# Scope
# def greet():
#     msg = 'a'
    
# print(msg)

#  Debbugging
def multiply(*numbers):
    total = 1
    # iterate
    for number in numbers:
        total *= number
    return total
    
print('start')
print(multiply(2, 3, 4, 5))