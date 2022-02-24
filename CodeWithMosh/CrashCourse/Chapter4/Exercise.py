# #-----------TRY IT YOURSELF---------#
# # 4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
# # Store these pizza names in a list, and then use a for loop to print 
# # the name of each pizza.
# pizzas = []
# pizzas.append('Dominos')
# pizzas.append('Papa john')
# pizzas.append('Pizza Hut')

# for pizza in pizzas:
#     print(pizza)

# # • Modify your for loop to print a sentence using the name of the pizza 
# # instead of printing just the name of the pizza. For each pizza you should 
# # have oneline of output containing a simple statement like I like 
# # pepperoni pizza.

# for pizza in pizzas:
#     print(f"I like to have {pizza.upper()} for a dinner tonight.")

# # • Add a line at the end of your program, outside the for loop, that states 
# # how much you like pizza. The output should consist of three or more lines 
# # about the kinds of pizza you like and then an additional sentence, such as 
# # I really love pizza!

# print(f"I really like {pizza} so much.")
# print(f'I love {pizzas}')


# #4-2. Animals: Think of at least three different animals that have a common 
# # characteristic. Store the names of these animals in a list, and then use a 
# # for loop to print out the name of each animal.
# pets = ['cat', 'dog', 'parrot']
# for pet in pets:
#     print(f"{pet.upper()}")

# # • Modify your program to print a statement about each animal, such as
# # A dog would make a great pet.
# print(f"{pets[0].title()} is so cute and always love to be pet.")
# print(f"{pets[1].title()} dislike strangers. He always barks at them.")
# print(f"{pets[2].title()} learning how to communicate with me.")

# # • Add a line at the end of your program stating what these animals have in 
# # common. You could print a sentence such as Any of these animals would make 
# # a great pet!

# print(f"{pets[0]}, {pets[1]}, {pets[2]}, are friendly animals.")

# #-----------TRY IT YOURSELF---------#

# #4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
# # inclusive.

# for i in range(1, 21):
#     print(i)

# #4-4. One Million: Make a list of the numbers from one to one million, and then 
# # use a for loop to print the numbers. (If the output is taking too long, stop it 
# # by pressing ctrl-C or by closing the output window.)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for num in numbers:
#     print(num)

# #4-5. Summing a Million: Make a list of the numbers from one to one million, and 
# # then use min() and max() to make sure your list actually starts at one and ends 
# # at one million. Also, use the sum() function to see how quickly Python can add 
# # a million numbers.
# print("The min number is:", min(numbers))
# print("The max numbers is:", max(numbers))
# print("The total sum of numbers os:", sum(numbers))

# #4-6. Odd Numbers: Use the third argument of the range() function to make a list 
# # of the odd numbers from 1 to 20. Use a for loop to print each number
# for odd in range(1, 21):
#     if odd % 2 == 1:
#         print(odd)
        
#         #OR
        
# oddNumbers = list(range(1,21, 2))
# print(oddNumbers)

# #4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print 
# # the numbers in your list.
# threes = list(range(3, 31, 3))
# print(threes)

# #4-8. Cubes: A number raised to the third power is called a cube. For example, 
# # the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes 
# # (that is, the cube of each integer from 1 through 10), and use a for loop to 
# # print out the value of each cube.
# cubes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for cube in cubes:
#     cube **= 3
#     print(cube) 

# #4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 
# # 10 cubes.
# cubes = [cube**3 for cube in range(1,11)]
# print(cubes)

#-----------TRY IT YOURSELF NUMBER LIST---------#

pets = ['cat', 'dog', 'parrot', 'rabit']

#4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
print(f"The first three items in the list are: {pets[:3]}.")

# • Print the message Three items from the middle of the list are:. Use a slice to 
# print three items from the middle of the list.
print(f"The three items from the middle of the list are: {pets[2:]}")
# • Print the message The last three items in the list are:. Use a slice to print 
# the last three items in the list.
print(f"The last three items in the list are: {pets[1:]}")

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). 
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the 
# following:
friend_pizzas = []
my_pizzas = ['Dominos',"papa john", 'pizzza hut']
friend_pizzas = my_pizzas[:]
print(friend_pizzas)
# • Add a new pizza to the original list.
my_pizzas.append('jimmy johns')

# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append('pieology pizza')
# • Prove that you have two separate lists. Print the message My favorite pizzas 
# are:, and then use a for loop to print the first list. Print the message My 
# friend’s favorite pizzas are:, and then use a for loop to print the second 
# list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)

print("\nMy freind's favorite pizzas are: ")
for pie in friend_pizzas:
    print(pie)
    
#4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing to save space. Choose a version of foods.py, and write 
# two for loops to print each list of foods.

foods = ['rice', 'sandwich', 'pizza', 'moi moi']
print("\n")
for food in foods:
    print(food)
    
    
print("\n")
foods = [food for food in list(foods)]
print(foods)

#-----------TRY IT YOURSELF TUPLE---------#

#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think 
# of five simple foods, and store them in a tuple.
buffets = ('pho', 'noodle', 'fried rice', 'pasta')
# • Use a for loop to print each food the restaurant offers.
print("\n")
for buffet in buffets:
    print(buffet)
    
# • Try to modify one of the items, and make sure that Python rejects the
# change.
    buffets[0] = 'yam'

# • The restaurant changes its menu, replacing two of the items with different 
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.
buffets = ('pounded yam', 'jalof rice', 'noodle', 'pasta')
print("\n")
for buffet in buffets:
    print(buffet)