# We can iterate through a dictionary using a for loop and return all keys present
user ={
    "id" : 1234,
    "fName": "Paul",
    "lName": "Miller",
    "age" : 25,
}
for key in user:
    print(key)

print("")
# We can also use the keys() function with a for statement to get all keys from a dictionary
for key in user.keys():
    print(key)

print("")
# We can also use the values() function with a for statement to get all values from a dictionary
for value in user.values():
    print(value)

print("")
# We can also use a for statement to get keys and values using the items() function
for key, value in user.items():
    print(key, value)

print("")
# Using a for statement, create a new dictionary of products with a 10% discount applied to the price of each product from the original dictionary
products={
    "external drive": 90,
    "bluetooth mouse": 70,
    "laptop bag": 25,
    "memory card": 30,
}
d_products = {} # New dictionary

for product, price in products.items():
    d_products[product] = price - (price * 0.10)

# Or we can use this
d_products = {product: price - (price * 0.10) for (product, price) in products.items() }

print(d_products)   # 列出打折后的价格表


print("")
# Copying dictionaries 复制字典
# 如果直接使用 = 复制字典，当 print 结果时不会出现异常
cp_products = products
print(cp_products["memory card"])
# 但如果要对字典中的 key 进行赋值，此时原字典中的值也会改变
# 注释：原来为 30
cp_products["memory card"] = 20
print(cp_products["memory card"]) # 20
print(products["memory card"])    # 20
# 因为这两个字典使用的是相同的字典对象

products={
    "external drive": 90,
    "bluetooth mouse": 70,
    "laptop bag": 25,
    "memory card": 30,
}
# 所以应该使用 copy() 而不是直接复制
cp_products = products.copy()
# 或者用 dict()
cp_products = dict(products)
cp_products["memory card"] = 20
if id(products) != id(cp_products):
    print("They are different.")


print("")
# Nested dictionaries 嵌套的字典
# 字典的内部也可以包含字典
cars = {
    "Kia": {"model": "Rio", "year": 2019, "colour": "black"},
    "VW": {"model": "Golf", "year": 2017, "colour": "blue"}
}
# 使用 type() 来查看变量的类别
print(type(cars["Kia"]))
print(type(cars["VW"]))

# 使用 [] 来访问嵌套字典中的内容
print(cars["Kia"]["model"])    # Rio
print(cars["VW"]["model"])     # Golf

print("")
# 向嵌套字典中添加内容，既可以每个键单独添加
cars["Nissan"] = {}
cars["Nissan"]["model"] = "Bluebird"
cars["Nissan"]["year"] = 1989
cars["Nissan"]["colour"] = "green"
# 也可以一次性添加所有键
cars["Nissan"] = {"model": "Bluebird", "year": 1989, "colour": "green"}

print(cars["Nissan"].items())
# Output: dict_items([('model', 'Bluebird'), ('year', 1989), ('colour', 'Green')])

# 同样也可以用 [] 来更改嵌套字典中特定键的值
cars["VW"]["colour"] = "green"
print(cars["VW"].items())

# 使用 del 来删除嵌套字典中的键
del cars["VW"]["colour"]
print(cars["VW"].items())

print("")
cars = {
    "Kia": {"model": "Rio", "year": 2019, "colour": "black"},
    "VW": {"model": "Golf", "year": 2017, "colour": "blue"}
}
# Iterate 迭代
for make, car, in cars.items(): 
    print(make, end =" ")
    for colour in car:
        print(car["colour"]) 
        break # 如果不在这里加入 break ，则程序会输出三次 colours （因为 Kia 或 VW 中有三个键）
# Output: Kia black
#         VW blue

# Nested dictionaries comprehension
mtable = {outer:{inner: outer * inner for inner in range (1,5)} for outer in range(1,4)}
print(mtable)

# 此外还有 fromkeys() 没有学习，需要的话可以去网上搜索