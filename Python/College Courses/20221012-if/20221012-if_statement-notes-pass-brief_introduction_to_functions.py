# if statement
# used to execute a block of code/set of instructions/statements, based on a specified condition

age = int(input())
ticket_price = 30 if age >= 18 else 15
print("The price of the ticket is ${}".format(ticket_price))

# Notes (requires at least Python 3.6)
Name = "JP"
Location = "Scotland"
cats = 2
print("{} lives in {} with {} cat(s).".format(Name, Location, cats))
# or we can use a f before the text:
print(f"{Name} lives in {Location} with {cats} cat(s).")
# or replace {} with %s/%d (Placeholder 占位符)
# s 代表字符串, d 代表十进制
print("%s lives in %s with %d cat(s)" %(Name, Location, cats))

# pass keyword does nothing
pass
# Useful when a statement is required syntactically but no action is required
# often uses as a placeholder for future code that is yet to be written

a = 10
b = 11
if a < b:
    pass  # Haven't decided what should happen here
    # 此处如果不加入 pass ，程序会报错
print("Not part of the if statement")


# A brief introduction to Functions
# A named block of code that return a value
# Allows us to reuse a block of code without having to copy and paste it throughout the source code
# It will only run when it is called
def jpsFunction():
# def represents define
# 这个函数不需要参数，仅在终端输出 Hello JC1001
    print("Hello JC1001")

jpsFunction()

def jpsFunction(name):
# 这个函数包含一个参数 name
    print(name)

jpsFunction("JP")
# 参数 name 的值为 JP ，会在终端输出 JP

def simpleAdd(a, b):
# 这个函数包含两个参数 a, b
    return a + b

simpleAdd(1, 2)
# 返回 a + b 的结果，注意并不会在终端输出结果

x = simpleAdd(1, 2)
print(x)
print(simpleAdd(1, 2))