# list
# Lists are ordered, the order of items is defined and will not change
# New items are added to the end of a list
# Note: some list methods can change the order but mostly the order of order of items will not change
# The item in the list can be added or removed

# Listed are created using square brackets [] (this one is more common)
degrees = ["AI", "IMIS", "SE"]
# or list() constructor
degrees = list(("AI", "IMIS", "SE"))

print(degrees)
# Output: ['AI', 'IMIS', 'SE']

print("")
# We can use lenth() to return the number of items in a list
print(len(degrees))
# Output: 3

# Items within a list can be of any data type
# Items can also be of different types
numList = [1, 2, 3, 4, 5]
strList = ["hey", "there", "ok"]
floatList = [0.414, 1.14514]
mixedList = [1, "hello"]


print("")
# Access list items
# List items are indexed, we can assess list elements using index numbers
# Items start at index number 0
# A negative index refers to the end of the list
aList = ["item1", "item2", "item3", "item4"]
print(aList[1])
# Output: item2
print(aList[-1])
# Output: item4

print("")
# We can specify a renge of indexes by indicating where to start and stop in a list
# By specifying a range we can return a new list with a specific collection of items
shopping = ["bread", "noodles", "soup", "apples", "potatoes", "peppers"]
print(shopping[2:5])
# Output: ['soup', 'apples', 'potatoes']
# If the end range is not included, the range will continue to the end of the list
print(shopping[3:])
# Output: ['apples', 'potatoes', 'peppers']
# Start range is the same
print(shopping[:3])
# Output: ['bread', 'noodles', 'soup']
# A negative index range can be used to retuen items starting from the end of the list
# Remember: the last item is not included
print(shopping[-3:-1])
# Output: ['apples', 'potatoes']

print("")
# We can check whether an item is included within a list using the in keyword
if "noodles" in shopping:
    print("noodles is in the shopping list")
# We can check whether an item is not included within a list using the not and in keyword
if "pasta" not in shopping:
    print("pasta is not in the shopping list")


print("")
# Modifying list items
# To modify a single item, we can change its value by referring to the list item index number
shopping = ["bread", "noodles", "soup", "apples", "potatoes", "peppers"]
shopping[3] = "lemon"
print(shopping)
# Output: ['bread', 'noodles', 'soup', 'lemon', 'potatoes', 'peppers']
#  We can also change items within a specific range of a list and create a new list with new values using the range which specifies where new items are to be positioned
shopping = ["bread", "noodles", "soup", "apples", "potatoes", "peppers"]
shopping[1:3] = ["pasta", "tomato"]
print(shopping)
# Output: ['bread', 'pasta', 'tomato', 'apples', 'potatoes', 'peppers']
# If we add less items than those we replace, the new items are inserted and the remaining list items are shifted
shopping = ["soup", "apples", "potatoes", "peppers"]
shopping[0:2] = ["lemon"]
print(shopping)
# Output: ['lemon', 'potatoes', 'peppers']

print("")
# Inserting list items
# We can insert a new item at a specific position without replacing existing items using the insert() function
shopping = ["soup", "apples", "potatoes", "peppers"]
shopping.insert(0, "noodle")
print(shopping)
# Output: ['noodle', 'soup', 'apples', 'potatoes', 'peppers']

# Add to a list
# We can add an item to the end of a list using append() function
shopping = ["soup", "apples", "potatoes", "peppers"]
shopping.append("noodles")
print(shopping)
# Output: ['soup', 'apples', 'potatoes', 'peppers', 'noodles']

# Extend a list using another list
# We can extend a list by appending items from another list using the extend() function
colours =["red","green","blue"]
moreColours = ["yellow","orange","purple"]
colours.extend(moreColours)
print(colours)
# Output: ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
# We can extend a list by appending items from any otheriterable using the extend() function
colours =["red","green","blue"]
moreColours = ("yellow","orange","purple")
colours.extend(moreColours)
print(colours)
# Output: ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

# Remove specific items from a list
# We can remove a specific item for a list
colours = ["red", "green", "blue"]
colours.remove("green")
print(colours)
# Output: ['red', 'blue']

# Removing item at specific index
# To remove an item from a specific index in a list, we use the pop() function
colours =["red","green","blue"] 
colours.pop(0)
print(colours)
# Output: ['green', 'blue']
# Remove last item with pop()
# Note: if no index is specified, the last item is removed
colours =["red","green","blue"] 
colours.pop()
print(colours)
# Output: ['red', 'green']

# Removing items using del()
# The del() function can also be used to remove an item at a specific index
colours =["red","green","blue"] 
del colours[0]
print(colours)
# Output: ['green', 'blue']

# The del() function can also be used to delete the entire list
colours =["red","green","blue"] 
del colours
# >>> print(colours) # will generate error
# NameError: name 'colours' is not defined

# Empty a list
# Th eclear() function can be used to empty a list
# Note: the list still exists but has no items
colours =["red","green","blue"] 
colours.clear()
print(colours)
# Output: []