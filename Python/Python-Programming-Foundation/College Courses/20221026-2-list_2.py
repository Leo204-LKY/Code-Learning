# Iterling through lists
# We have already seen how we can iterate through a list to reveal each individual item:
colours = ["red", "green", "blue"]
for colour in colours:
    print(colour)
# Output: red
#         green
#         blue

print("")
# We can use the len() and range() function to create an iterable that we can use to print each item of a list
colours = ["red", "green", "blue"]
for colour in range(len(colours)):
    print(colours[colour])
# Output: red
#         green
#         blue

print("")
# List comprehension
# We can also use list comprehensions via a short-hand for loop for more concise syntax
colours =["red", "green", "blue"]
[print(colour) for colour in colours]
# Output: red
#         green
#         blue

print("")
# List comprehensions provide more concise syntax for creating a new list from the items of an existing list
# e.g. Create a new list of names which contains only names which include a “b”
names =["alan", "bob", "brian", "charlie", "jacob"] 
bNames = [] #empty list
for n in names: 
    if "b" in n:
        bNames.append(n)
print(bNames)
# Output: ['bob', 'brian', 'jacob']

# With list comprehension, we can do this in a single line of code
# [expression for item in iterable if condition == True]
# The condition acts as a filter that only adds items to the new list is the items evaluate to True
# Note the condition is optional
names =["alan", "bob", "brian", "charlie", "jacob"]
bNames = [n for n in names if "b" in n]
print(bNames)
# Output: ['bob', 'brian', 'jacob']

# The list comprehension expression, is the current list item iterated
# This is also the outcome and can be manipulated prior to being added to a new list
# e.g. change the case of the first letter
names =["alan", "bob", "brian", "charlie", "jacob"] 
bNames = [n.capitalize() for n in names if "b" in n] 
print(bNames)
# Output: ['Bob', 'Brian', 'Jacob']

# We can also use conditional statements to modify the current item iterated and manipulate the outcome
# e.g. return the item if the name is not bobby, if it is bobby, return bob
names =["alan", "bobby", "brian", "charlie", "jacob"] 
otherNames = [n if n != "bobby" else "bob" for n in names] 
print(otherNames)
# Output: ['alan', 'bob', 'brian', 'charlie', 'jacob']


print("")
# List sorting
# The sort () function is available for all list type objects
animals = ["reptile","cat","penguin","dog","birds"] 
animals.sort()
print(animals)
# Output: ['birds', 'cat', 'dog', 'penguin', 'reptile']
scores = [59, 11, 72, 8, 91, 33]
scores.sort() 
print(scores)
# Output: [8, 11, 33, 59, 72, 91]

# We can use the reverse keyword to change the default sort
animals = ['birds', 'cat', 'dog', 'penguin', 'reptile']
animals.sort(reverse = True)
print(animals)
# Output: ['reptile', 'penguin', 'dog', 'cat', 'birds']


# List function summary
# | Function  | Description                                                   |
# | append()  | Add an item to the end of a list                              |
# | clear()   | Empty a list of all items                                     |
# | copy()    | Return a copy of a list                                       |
# | count()   | Return the number of items within a specified value           |
# | extend()  | Add the elements of a list or any other iterable to a list    |
# | index()   | Returns the index of the first element with a specified value |
# | insert()  | Adds an element as a specified position                       |
# | pop()     | Remove an item at a specified position                        |
# | remove()  | Remove an item at a specified position                        |
# | reverse() | Reverse the order of a list                                   |
# | sort()    | Sort a list                                                   |