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

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to 
# send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the 
# name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

family = ['Baba', 'Karima', 'Mustapha']
print(family)
cant_makeit = family.pop(0)
print(f"{cant_makeit.title()} can't make it to the dinner, because his sick.")
print(family)
family.insert(0, 'Mama')
print(f"new invited guests list is: {family}")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() 
# call to the end of your program informing people that you found a bigger dinner table.
family = ['Mama','Karima','Mustapha']
print(f"At {family[0]}, {family[1]}, {family[2]} We inviting more guests because we got more space for the dinner.")

# • Use insert() to add one new guest to the beginning of your list.
family.insert(0, 'Baba')
print(family)

# • Use insert() to add one new guest to the middle of your list.
family.insert(2, 'Yusuf')
print(family)

# • Use append() to add one new guest to the end of your list.
family.append('Saifullah')
family.append('Muhammad')
family.append('Abdulmumini')

# • Print a new set of invitation messages, one for each person in your list.
print(family)
print(f"{family[0]}, {family[1]}, {family[2]}, {family[3]}, {family[4]}, {family[5]}, {family[6]}, {family[7]}, you are all invited to our annual family dinner")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests.
print(family)
# • Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.
print(f"Sorry the dinner table wont arrive soon, so I only have space for two guests.")

# • Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner.
print(family)
listpop1 = family.pop()
print(f"{listpop1} I'm so sorry for the inconvience.")
listpop2 = family.pop()
print(f"{listpop2} I'm so sorry for the inconvience.")
listpop3 = family.pop()
print(f"{listpop3} I'm so sorry for the inconvience.")
listpop4 = family.pop()
print(f"{listpop4} I'm so sorry for the inconvience.")
listpop5 = family.pop()
print(f"{listpop5} I'm so sorry for the inconvience.")
listpop6 = family.pop()
print(f"{listpop6} I'm so sorry for the inconvience.")

print(family)

# • Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
print(f"{family[0]}, {family[1]}, you are still invited to the dinner.")
print(family)

# • Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end 
# of your program.
del family[0]
del family[0]
print(family)