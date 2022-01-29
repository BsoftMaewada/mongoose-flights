#Primitive Types
#Strings
# course = "Python Programming"
# print(len(course)) #print 18
# print(course[0])   #
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])
# print(course[:])

#Escape Sequence
# course = "Python \"Programming"
# course = "Python \'Programming"
# course = "Python \\ Programming"
# course = "Python \nProgramming"
# print(course)

#Formatted Strings
# first = "BUHARI"
# last = "MAIWADA"

# # full = first +' ' + last 
# full = f"{first} {last}"

# print(full)

#Strings Methods
course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip()) # remove whitespace 
print(course.find('Pro'))
print(course.replace('P' , 'J'))

#numbers
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

#Working with numbers
import math

print(round(2.9))
print(abs(-2.9))

print(math.sqrt(4))

#Type Conversion
# x = input('x: ')
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

##CONTROL FLOW
#Comparison operator
10 > 3
10 < 2
10 == 10
10 != "10"
'bag' == 'BAG'

#Condition statement

temperature = 23
if temperature > 35:
    print("It's warm")
    print("Drink water")
elif temperature < 20:
    print("It's nice")
else:
    print ("Its cold")
    
#Ternsry operators
age = 22

# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

#        OR
message = "Eligible" if age >= 18 else "Not eligible"
print (message)

#LOGICAL OPERATORS

#and
high_credit = False
good_credit = True

if high_credit and good_credit:
    print("Eligible")
else:
    print("Not eligible")
    
#or
high_credit = True
good_credit = True

if high_credit or good_credit:
    print("Eligible")
else:
    print("Not eligible")
    
#Not 

high_credit = True
good_credit = True
student = True

if high_credit and good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")
    
#chaining comparison operator
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")
    
##QUIZ
if 10 == "10": # not equal
    print("a")
elif "bag" > "apple" and "bag" > "cat": # if true and false which is FALSE
    print ("b")
else:
    print("c")
    
#For Loops
for number in range(3):
    # print("Atempt", number)
    print("Atempt",number, (number + 1) * ".")
    
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for numb in my_list:
#     print(numb)

for numb in my_list:
    # print('hello world')
    if numb % 2 == 0:
        print(numb,' is an even number')
        
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]       
my_sum = 0


for numb in my_list:
    my_sum += numb
print(my_sum)
    
#For Else

successful = False
for number in range(3):
    print("Atempt")
    if successful:
        break
else:
    print("Attempted 3 times but failed!")

# #Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
        
#for loop iterations
for y in ('PY4U.net'):
    print(y)

my_tupple = (1, 2, 3)
for j in my_tupple:
    print(j)
    
# print(type(5))
# print(type(range(5)))

# for x in range(5):

#     if num == 1:
#         return (type (str(1)))
    
#WHILE LOOP
# continious execution

number = 100
while number > 0:
    print(number)
    number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

#infinite loop

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break


my_num = int(input('Please Enter a number: '))
#even numbers block
if my_num % 2 == 0:
    if my_num > 5:
        print('yes')
    else:
        print('none')
#odd numbers block
if my_num % 2 == 1:
    if my_num < 5:
        print ('yes')
    else:
        print ('none')
        
#without nested loops

if my_num % 2 == 0 and my_num > 5:
    print('yes')
else:
    print ('none')
    
if my_num % 2 == 1 and my_num < 5:
    print ('yes')
else: 
    print ('none')

#Ternsry method
my_num = int(input('Please Enter a number: '))
    
my_num ='yes' if my_num % 2 == 0 and my_num < 5 else 'none'

# my_num = 'no' if my_num % 2 == 1 and my_num < 5 else 'none'


#EXERCISE
count = 0
for k in range(1, 10):
    if k % 2 == 0:
        count += 1
        print(k)
print(f"We have {count} even numbers") 

count = 0
while  count < 7:
    print(count)
    count += 1
    
#Nested loop 
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8]
list_3 = []

for v in list_1:
    for z in list_2:
        list_3.append(v*z)
print(list_3)

