# ############################ HCF/GCD OF TWO NUMBERS ####################################

# def comp_HCF(x,y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
        
#     for i in range(1, smaller + 1):
#         if (( x % i == 0) and (y % i == 0)):
#             gcd = i
#     return gcd

# num1 = int(input("Enter a value: "))
# num2 = int(input("Enter a value: "))
# print("The GCD of ", num1, " and " , num2, " is ", comp_HCF(num1, num2),) 

############################ LCM OF TWO NUMBERS ####################################

# def find_LCM(a, b):
#     if a > b:
#         greater = a
#     else:
#         greater = b
    
#     while(True):
#         if ((greater % a == 0) and (greater % b == 0)):
#             lcm = greater
#             break
            
#         greater += 1
#     return lcm
# n1 = int(input("Enter a value: "))
# n2 = int(input("Enter a value: "))
# print("The LCM of ", n1, " and " , n2, " is ", find_LCM(n1, n2)) 

# ############################ Fibonacci ####################################

# def fib(num):
#     a, b = 0, 1
    
#     for i in range(1, num + 1):
#         print(a, end=" ")
        
#         c = a + b
#         a = b
#         b = c

# num = int(input("Enter a value: "))
# fib(num)
# print("\n")

# ############################ EVEN NUMBER ####################################

# def EvenNumber(num):
#     return (num % 2 == 0)

# num =int(input("Enter a number: "))
# if EvenNumber(num):
#     print(num,"Even number")
# else:
#     print(num, "is not even")

## /****** For range of even numbers *******/ ##

# n = int(input("Enter a value: "))
# k = int(input("Enter a value: "))

# for i in range(n, k):
#     if i % 2 == 0:
#         print(i, end=" ")
# print("\n")

# ############################ OOD NUMBER ####################################

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# for i in range(num1, num2):
#     if i % 2 != 0:
#         print(i, end=" ")
# print("\n")

# ############################ EVEN AND OOD NUMBER ####################################

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))

# for i in range(x, y):
#     if i % 2 == 0:
#         print(i, "is an even number")
#     else:
#         print(i, "is an odd number")
        
# ############################ LARGEST NUMBER ####################################
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter a number: "))
# n3 = int(input("Enter a number: "))

# if (n1 > n2) and (n1 > n3):
#     print("The largest is ", n1)
# elif (n2 > n1) and (n2 > n3):
#     print("The largest is ", n2)
# else:
#     print("The largest is ", n3)
    
# ############################ CHECK IF A STRING IS PANGRAM ####################################

# def isPangram(pangram):
#     c=0
#     s=set()
#     for xx in pangram.lower():
#         x = ord(xx) - ord('a')
#         if x not in s and x>=0 and x<26:
#             c+=1
#             s.add(x)
#             if c==26:
#                 break;
#     return c==26

# print(isPangram(input()))

# ############################ GRAMMER ####################################

# def checkGrammer(inputString1):
#     i = inputString1
#     print(i)
#     if i == '{}':
#         return "Set"
#     elif i == '(,)':
#         return "Set"
#     elif i=='{,,}':
#         return "Not Set"
#     elif i[0] == '{' and i[-1] == '}':
#         return "Set"   
#     else:
#         return "Not Set"
    
    
############################ WORD PROBLEM ####################################

# def wordBreak(wordList, word):
#     if word == '':
#         return True
#     else:
#         wordLen = len(word)
#         x=[(word[ :i] in wordList) and wordBreak(wordList, word[i: ]) for i in range(1, wordLen+1)]
#         print(x)
#         return any(x)
# print(wordBreak(["IBM", "I", "LOVE", "And", "World"], "ILoveIBMAndWorld"))

# ##### Another way ######
# def wordBreak(wordList, word):
#     if word == '':
#         return True
#     else:
#         wordLen = len(word)
#         res = False
#         for i in range(1, wordLen+1):
#             if [(word[ :i] in wordList) and wordBreak(wordList, word[i: ])]:
#                 return True
#         return False
# print(wordBreak(["IBM", "I", "LOVE", "And", "World"], "ILoveIBMAndWorld"))

############################ LONGEST PALINDROME ####################################

#BRUTE FORCE APPROACH

# # s = "damadamda" #for a giving word
# s = str(input("Enter a word: ")) #for user input
# print()

# maxLength =0
# maxString = ""
# for i in range(len(s)): #start from the left end
#     for j in range(len(s) - 1, i, -1): #start from the right end
#         if s[i] == s[j]:
#             x = i
#             y = j
#             while x < y and s[x] == s[y]:
#                 x += 1
#                 y -= 1
#                 if x == y or x > y:
#                     if j - i + 1 > maxLength:
#                         maxLength = j - i + 1
#                         maxString = s[i:j + 1]
# print(maxLength)
# print(maxString)

#BRUTE FORCE APPROACH USING FUNCTION

# maxLength =0
# maxString = ""
# def findPilindrome(s):
#     for i in range(len(s)): #start from the left end
#         for j in range(len(s) - 1, i, -1): #start from the right end
#             if s[i] == s[j]:
#                 x = i
#                 y = j
#                 while x < y and s[x] == s[y]:
#                     x += 1
#                     y -= 1
#                     if x == y or x > y:
#                         return s[i:j + 1]
#     return ""

# print(findPilindrome("adnmadamad"))

#DYNAMIC APPROACH

# def LongestPilindrome(s):
#     n = len(s)
#     ms = [0,0]
#     dp = [[0 for i in range(n)] for j in range(n)] #creating array
#     for i in range(n): #size
#         for j in range(n-i): # j is our staring index
#             if i == 0:
#                 dp[j][j]=1
#             elif i == 1:
#                 if s[j] == s[j+i]:
#                     dp[j][j+i]=1
#                     if j+i-j+1 > ms[1] - ms[0]+1:
#                         ms = [j, j+i]
#             elif s[j] == s[j + i] and dp[j+1][j+i - 1] == 1:
#                 dp[j][j+i] = 1
#                 if j+i-j+1 > ms[1]- ms[0]+1:
#                     ms = [j, j+i]
#     return s[ms[0]: ms[1] + 1]

# print(LongestPilindrome(input()))

###### PALINDROME ALGORITHM ######
#
# input: string phrase
# output: true/false

# let length = phrase.length
# let c = 0

# while (c <= length/2){
#     if(phrase[c] != phrase[length -1 - c])
#         return False
#     c = c + 1
# }

# return True
#*/
############################ CORONAVIRUS CONDITION ####################################

# Vaccine drive list preparator
# def func(a, d, c):
#     La = len(a)
#     Ld = len(d)
#     if not(La == 14 or Ld == 10 or c == "no" or c == "yes"):
#         print("Invalid Input")
#     else:
#         p = d.split("/")
#         age= 2021 - int(p[-1])
#         if age > 60 or c == "yes":
#             print(1)
#         elif age > 45:
#             print(2)
#         elif age > 30:
#             print(3)
            
# func("6785 3456 1337", "03/12/1972", "yes")

############################ Square Pattern with NUMBERS ####################################

rows = int(input("Enter a number of rows: "))

for i in range(1, rows +1):
    for j in range(1, rows +1):
        if j <= i:
            print(i, end=" ")
        else:
            print(j, end=" ")
    print()
