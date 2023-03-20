# Dictionaries 字典
# A dictionary is used to store data values in key value pairs
# A key value pair are two related data items (key:value)
  # A key is usually a constant that defines the data e.g. Name
  # A value is usually the data itself   e.g. js
    # Name: JS
    # Age: 32
# Dictionaries as of Python 3.7 are ordered but in Python 3.6 and earlier, dictionaries are unordered
# Dictionary items can be changed
# A Dictionary cannot contain duplicates

# Creating a dictionary
book = {
    "title": "Programming in Python",
    "publisher": "Jamiesons",
    "year": 2021,
}
print(book)
# Output: {'title': 'Programming in Python', 'publisher': 'Jamiesons', 'year': 2021}
print(len(book))
# Output: 3

# Dictionary items can be of any data type including lists types
book = {
    "title":"Programming in Python", 
    "publisher": "Jamiesons", 
    "year": 2021,
    "availability": ["online", "hardback", "PDF"]
}
# We can access dictionary items using keys
print(book["publisher"])
# Output: Jamiesons
# We can also use the get() function to access items
print(book.get("year"))
# Output: 2021

# The keys() function can be used to retuen a list of keys in the dictionary
print(book.keys())
# Output: dict_keys(['title', 'publisher', 'year', 'availability'])

print("")
# If we add a new item, we can see how the list of keys gets updated
book = {
    "title": "Programming in Python",
    "publisher": "Jamiesons",
    "year": 2021
}
print(book.keys())
# Output: dict_keys(['title', 'publisher', 'year'])
book["availability"] = "online"
print(book.keys())
# Output: dict_keys(['title', 'publisher', 'year', 'availability'])

print("")
# Get values
# The values() function will return a list of all values in the dictionary
print(book.values())
# Output: dict_values(['Programming in Python', 'Jamiesons', 2021, 'online'])

# Get items
# The items() function will return each item in a dictionary, as tuples in a list
print(book.items())
# Output: dict_items([('title', 'Programming in Python'), ('publisher', 'Jamiesons'), ('year', 2021), ('availability', 'online')])


print("")
# Check if Key exists / is present
if "title" in book:
    print("Title key is present in book")


# Ordered vs unordered
# In Python 3.7 dictionaries are ordered but in Python 3.6 and earlier, dictionaries are unordered
# Ordered dictionary
  # Have a defined order that does not change
# Unordered dictionary
  # No defined order and items cannot be referred to using an index


print("")
# Changing items
# We can change dictionary items using keys
book["title"] = "Python programming"
# We can also use update() function
book.update({"title":"Python programming"})
print(book["title"])
# Output: Python programming

# Duplicate keys
# Dictionaries cannot have contain two items with identical keys # keys are unique
# Duplicate keys will overwrite existing values (data loss!)
book = {
    "title":"Programming in Python", 
    "title": "Python so and so",  # overwrite the previous one
    "publisher":"Jamiesons",
    "year": 2021
}
print(book["title"]) 
# Output: Python so and so

print("")
# We can add items using a new key with an assignment statement to give it a value
book = {
    "title":"Programming in Python", 
    "publisher":"Jamiesons",
    "year": 2021
}
book["availability"] = "online" 
# or update() function
book.update({"availability":"online"})
print(book)
# Output: {'title': 'Python so and so', 'publisher': 'Jamiesons', 'year': 2021, 'availability': 'online'}

print("")
# Removing items
# The pop() function can be used to remove specific items using the key as a parameter
book.pop("availability")
print(book)
# Output: {'title': 'Python so and so', 'publisher': 'Jamiesons', 'year': 2021}
# The popitem() function will
  # Remove and return the last item as of Python 3.7
  # Remove and return an arbitrary key/value pair, in versions earlier than Python 3.7
book.popitem()
print(book)
# Output: {'title': 'Python so and so', 'publisher': 'Jamiesons'}
# We can also remove specific items using the del keyword
book = {
    "title":"Programming in Python", 
    "publisher":"Jamiesons",
    "year": 2021,
    "availability": "online"
}
del book["availability"] 
print(book)
# Output: {'title': 'Programming in Python', 'publisher': 'Jamiesons', 'year': 2021}
# We can also remove the dictionary completely using the
del book
# >>> print(book) # generates error since book is removed completely
# NameError: name 'book' is not defined

# The clear function can be used to empty a dictionary
book = {
    "title":"Programming in Python", 
    "publisher":"Jamiesons",
    "year": 2021,
}
book.clear()
print(book)
# Output: {}