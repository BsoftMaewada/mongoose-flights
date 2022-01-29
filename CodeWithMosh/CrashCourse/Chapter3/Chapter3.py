#----------- LISTS ------------#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#Accessing Element in a list
print(bicycles[0])
print(bicycles[0].title())

print('=======================')
#index Position 
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

print('=======================')
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

#Changing, Adding and Removing elements
print('=======================')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Appending element to the end of the list
motorcycles.append('ryder')
print(motorcycles)

#inserting element into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'jincheng')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#Removing an item using the pop() method.
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print(f"The last motorcycle I owned was {popped_motorcycles}")

#Removing item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
