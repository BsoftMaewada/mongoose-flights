#For Loops

for number in range(3):
    print("Atempt")
for number in range(3):
    print("Atempt", number)
for number in range(3):
    print("Atempt", number + 1)
for number in range(3):
    print("Atempt", number + 1, (number + 1) * "." )
for number in range(1, 4):
    print("Atempt", number, number * "." )
for number in range(1, 10, 2):
    print("Atempt", number, number * "." )
    
#For Else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
    
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3x and failed")

#Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
        
#Iterations

for x in "PYTHON":
    print(x)
for y in [1, 2, 3, 4, 5]:
    print(y)
#e.g
# for item in shopping_cart:
#     print(item)

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
        
print(f"we have {count} numbers")    

#functions
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    
greet("Buhari", "Maiwada")


def fizz_buzz(input):
    for input in range(100):
        if input % 3 == 0 and input % 5 == 0:
            print("fizzBuzz") 
        elif input % 3 == 0:
            print("fizz")
        elif input % 5 == 0:
            print("buzz")
        else:
            print(input)
print(fizz_buzz(input))

# OR

def fizzBuzz(i):
    if (i % 2 == 0) and (i % 4 == 0):
        return "FizzBuzz"
    if i % 2 == 0:
        return "Fizz"
    if i % 4 == 0:
        return "Buzz"
    return i
print(fizzBuzz(30))

# def positive_integer(n):
#         if n % 2 != 0:
#             return "WEIRD"
#         if n % 2 == 0 and n == range (2, 5):
#             return "NOT WEIRD" 
#         if n % 2 == 0 and n == range (6, 20):
#             return "WEIRD" 
#         if n % 2 == 0 and n > 20:
#             return "NOT WEIRD"
#         return n
            
# # print(positive_integer(100))

            