#---------------- TRY IT YOURSELF -------------#

#VARIABLES

#2-1. Simple Message: Assign a message to a variable, and then print that 
# message.

biginner = "Hello World!"
print(f"{biginner} of programmers.")

#2-2. Simple Messages: Assign a message to a variable, and print that message. 
# Then change the value of the variable to a new message, and print the new 
# message.

change = "old message"
print(f"This is an {change}.")

change = "new message"
print(f"This is a {change}.")

# STRINGS

#2.3. Personal Message: Use a variable to represent a person’s name, and 
# print a message to that person. Your message should be simple, such as, 
# “Hello Eric, would you like to learn some Python today?”

name = "Eric"
personalMessage = f"Hell {name}, would you like to learn python today?"
print(personalMessage)

#2-4. Name Cases: Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.

nameCase ="Buhari Maiwada" 
print(nameCase.lower())
print(nameCase.upper())
print(nameCase.title())
print(nameCase.capitalize())

#2-5. Famous Quote: Find a quote from a famous person you admire. 
# Print the quote and the name of its author. Your output should look 
# something like the following, including the quotation marks:

        #Albert Einstein once said, “A person who never made a 
        # mistake never tried anything new.”
        
FamousPerson = "Albert Einstein"
FamousQuote = "A person who never made a mistake never tried anything new."
print(f'{FamousPerson} once said, "{FamousQuote}"')

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous 
# person’s name using a variable called famous_person. Then compose your message 
# and represent it with a new variable called message. Print your message.

famous_person = "Prophet Muhammad (SAW)"
message = "Love your parent and be nice to them."
print(f'{famous_person} once said, "{message}"')

#2-7. Stripping Names: Use a variable to represent a person’s name, and include 
# some whitespace characters at the beginning and end of the name. Make sure you 
# use each character combination, "\t" and "\n", at least once.
    #Print the name once, so the whitespace around the name is displayed. 
    # Then print the name using each of the three stripping functions, lstrip(), 
    # rstrip(), and strip().

person_name= "\tBuhari \nMaiwada "
print(person_name)
print(person_name.rstrip())
print(person_name.strip())

#NUMBERS

#2-8. Number Eight: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8. Be sure to enclose your operations 
# in print() calls to see the results. You should create four lines that look like 
# this:
                    #print(5+3)
#Your output should simply be four lines with the number 8 appearing once on each 
# line.

print(6 + 2)
print(10 - 2)
print(2 * 4)
print(16 // 2)

#2-9. Favorite Number: Use a variable to represent your favorite number. Then, 
# using that variable, create a message that reveals your favorite number. Print 
# that message.

favoriteNumber = 7
print(f"My favorite number is: {favoriteNumber}")

#The Zen of Python
import this