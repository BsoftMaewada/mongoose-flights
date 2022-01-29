#LIST

letters = ["a", "b", "c", "d", "e", "f"]
matrix =[[0, 1],[2, 3],[4, 5]]
zero = [0] * 100
combined = zero + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(chars)
print(len(chars))

# Accessing Items
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[0])
print(letters[-1])
#Accessing individual items
letters[0] = "A"
print(letters)
#To slice items
print(letters[0:3])
print(letters[:3])
#skip item by 2
print(letters[::2])

numbers = list(range(20))
print(numbers)
#will print every other number
print(numbers[::2])
#reverse order
print(numbers[::-1])

# 3 - List Unpacking
number = [1, 2, 3]
first, second, third = number
first, second, *other = number
# first = number[0]
# second = number[1]
# third = number [2]

print(first)
print(other)

# 4 - Looping over list

letters = ["a", "b", "c", "d", "e", "f"]

for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)
    
# 5 - Adding and removing item

letters = ["a", "b", "c", "d", "e", "f"]

# Add
letters.append("g")
letters.insert(0, "-")

# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()

print(letters)

# 6 - Finding Items
letters = ["a", "b", "c", "d", "e", "f"]
print(letters.index("d"))

print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))
