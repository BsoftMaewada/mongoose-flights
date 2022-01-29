#--------------- TRY IT YOURSELF -----------------#
#3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

friends = ['Affo', 'Auwal', 'Dansira', "Abdurrazak"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#3-2. Greetings: Start with the list you used in Exercise 3-1, 
# but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be 
# personalized with the person’s name.

message = f"I hope you having a nice day {friends[0]}"
print(message)

message1 = f"I hope you having a nice day {friends[1]}"
print(message1)

message2 = f"I hope you having a nice day {friends[2]}"
print(message2)

message3 = f"I hope you having a nice day {friends[3]}"
print(message3)

#3-3. Your Own List: Think of your favorite mode of transportation, such as 
# a motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.”

cars = []
cars.append('tesla')
cars.append('cadillac lyric')
cars.append('vinfase')
print(cars)

own_car = f"I would like to own a {cars[1]} 2022."
print(own_car)

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner. Then use your list to print a message to each person, inviting 
# them to dinner.

family = ['Baba', 'Karima', 'Mustapha']
print(f"You are cordially invited to family dinner {family[0]}, hope to see you soon insha ALLAAH.")
print(f"You are cordially invited to family dinner {family[1]}, hope to see you soon insha ALLAAH.")
print(f"You are cordially invited to family dinner {family[2]}, hope to see you soon insha ALLAAH.")
