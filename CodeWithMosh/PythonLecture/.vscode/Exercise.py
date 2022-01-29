def fizz_buzz(input):
    for input in range(100):
        if input % 3 == 0 and input % 5 == 0:
            print(input, 'fizzBuzz')
        elif input % 3 == 0:
            print(input, 'fizz')
        elif input % 5 == 0:
            print(input, 'buzz')
        else:
            print (input)
print(fizz_buzz(input))


# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return 'fizzBuzz'
#     elif input % 3 == 0:
#         return 'fizz'
#     elif input % 5 == 0:
#         return 'buzz'
#     return input

# print(fizz_buzz(10))

#RADIUS OF A CIRCLE
# def findArea():
#     radius = 10
#     pi = 3.1459
#     area = pi * radius * radius
#     print(area)
    
# def findArea(radius):
#     pi = 3.14
#     area = pi * radius * radius
#     return area

# # findArea(10)
# print(findArea(10))

# #GLOBAL vs LOCAL
# myVariable = 7
# myParam = 10

# def func1(myParam):
#     # global myVariable
#     myVariable = 20
#     print(myParam)
# func1(5)
# print(myVariable)