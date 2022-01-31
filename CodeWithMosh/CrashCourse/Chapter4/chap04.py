# #-----------  WORKING WITH LISTS ------------#

# magicians = ['alice', 'david', 'carolina']

# for magician in magicians:
#     print(magician)
    
    
# for magician in magicians:
#     print(f"{magician.title()}, that was a good trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print("Thank you, everyone. That was a great magic show!")

# #-----------  MAKING NUMERICAL LISTS ------------#

# #Using the range() function

# for value in range(1, 5):
#     print(value)

# #to print the value from 1-5 exact
# for value in range(1, 6):
#     print(value)
    
# #Using a range() to make a list
# numbers = list(range(1, 6))
# print(numbers)

# even_nubers = list(range(2, 11, 2))
# print(even_nubers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# #OR

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)

# #LIST COMPREHENSION

# squares = [value **2 for value in range(1, 11)]
# print(squares)

# #SLICE

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

# print(players[1:4])

# print(players[:4])

# print(players[2:])

# print(players[-3:])

# #Looping through a Slice

# players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())
    
# #Copy a list

# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods [:]

# print("My favorite foods are:")
# my_foods.append('cannoli')
# print(my_foods)

# print("\nMy friend's favorite food are:")
# friend_foods.append('ice cream')
# print(friend_foods)


#-----------  TUPLES ------------#

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#when we try to change item in tuples
# not possible
# dimensions[0] = 250


for dimension in dimensions:
    print(dimension)
    
#Writing over a tuple
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions =(400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)