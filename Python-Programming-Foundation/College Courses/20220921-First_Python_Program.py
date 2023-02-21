message = "Hello Python"
print(message)

message = "This is JC1001 course on python"
print(message)

# This is a comment.

a = 3 + 3 # Addition
b = 4 / 2 # Division
c = 10 % 3 # Modulo operator 取余
d = 4 // 2 # Floor division
e = (3 + 3) / 2 # Addition before division

name = input("Please enter your name: ")
message = "Hello " + name + "!"
print(message)

number = int(input("Please enter any number: "))
if not number < 10:
    print("The number is not less than 10!")
elif number == 10:
    print("The number is exactly 10!")
else:
    print("The number is less than 10!")