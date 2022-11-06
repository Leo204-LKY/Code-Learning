# https://pythontutor.com/
# 这个网站可以很直观的看到程序执行情况

# Functions 函数
# 函数是一段可重复使用的代码块
x = 1
y = 1
# x 和 y 是全局变量 Global variables，稍后再讲

def myFunction(a, b):
    a + b

print(myFunction(x, y))
# Output: None

# 问题在于，函数的最后应该返回一个值，这里即为 a + b 的值
def myFunction(a, b):
    return a + b

print(myFunction(x, y))
# Output: 2

# 函数返回的值也可以用于赋值
a = myFunction(x, y)
print(a)

print("")
# 如果一个函数需要四个输入值，但实际只输入了三个，则程序会报错
# 在参数前使用 * 来代表参数的数量不确定，此时会将变量打包为元组
def sumFunction(*a):
    return sum(a)

b = sumFunction(9, 1)
print(b)
# Output: 10

# 输出元组中的第一个数
def sumFunction(*a):
    return a[0]

b = sumFunction(1, 2, 3)
print(b)

# 通常 *a 会被替换为 *args (Arguments)
def sumFunction(*args):
    acc = 0
    for i in range(0, len(args)):
        acc += (args[i])
    return acc

print(sumFunction(57, 1))

# 我们也可以将键作为参数传递
def sumFunction(k1, k2):
    return k1 + k2

print(sumFunction(k1 = 57, k2 = 1))

# 如果参数数量不定，则可以使用键将字典传递给函数
# 常用 **kwargs (Keyword Arguments)
def sumFunction(**kwArgs):
    return kwArgs["dkey1"] * kwArgs["dkey2"]
# ** 代表将所有的数据打包为键值对数据，在函数体内实现解包

print(sumFunction(dkey1= 5,dkey2 = 10))
# 用键来传递参数，可以更好的理解各个参数的意义