# Tuples, sets and exceptions
# 元组、集合和异常

# 元组 Tuple
# 元组用于在一个变量中存储多个项
# 元素是一个有序且不可修改的集合
# 使用 () 来创建元组
aTuple = ("Python", "Java", "PHP")
# 元组的顺序是固定的，且不会改变
# 也就是说，元组创建后不能添加或移除项
# 元组是有索引的，因此可以具有相同值的项目
aTuple = ("Python", "Java", "PHP", "Python")

# 元组长度
# 可以用 len() 来获取元组的长度
aTuple = ("Python", "Java", "PHP", "Python")
print(len(aTuple))
print("")

# 包含单个元素的元组，需要包含逗号，否则就不是元组
aTuple = ("python",)
print(type(aTuple))  # <class 'tuple'>
aTuple = ("python")
print(type(aTuple))  # <class 'str'>
print("")

# 元组可以包含任何类别的项，也可以混合
myTuple = ("one", "two", "three") 
yourTuple = (1,2,3)
theirTuple = (True, True, False) 
mixedTuple = (True, 1, "one", False)

# 也可以使用 tuple() 构造函数来创建元组
someTuple = tuple(("this", "is", "a", "tuple"))

# 访问元组
# 使用与访问列表类似的方法来访问元组
# 元组索引从 0 开始
# 负数索引从最后一项开始
# 支持范围索引
# 也可以查询某项是否在元组内
t = ("one", "two", "three")
if "one" in t:
    print("yes")
print("")

# 修改元组？
# 元组是不可改变的(immutable)
# 但是我们可以创建列表，对列表进行修改后再创建另一个元组
a = ("one", "two", "three")
b = list(a)
b[2] = "four"
a = tuple(b)
print(a)
print("")

# 打包和解包(Packing and unpacking)
# 元组赋值被称为打包：
a = ("one", "two", "three")
# 我们还可以将值解包到变量中，也称为解包:
# 注意，我们必须将变量的数量与元组中值的数量相匹配
a = ("one", "two", "three")
(one,two,three) = a 
print(one) 
print(two) 
print(three)
# 如果变量的数量少于值的数量，可以在变量名后面使用*，将值作为列表分配给变量
thetuple = ("one", "two", "three", "four", "five")
(one,two,*three) = thetuple
print(one)     # one 
print(two)     # two
print(three)   # ['three', 'four', 'five']
print("")

# 与列表一样，元组也可以使用 for 或 while 语句来对元组进行循环
# 元素也可以相乘
a = ("something","another thing")
a = a * 2
print(a) # ('something', 'another thing', 'something', 'another thing')
print("")

# 元组 count() 和 index()
# count 方法返回特定值的出现次数
# index 方法返回指定变量的位置
a = (1, 2, 2, 3, 4)
print(a.count(2))   # 2
print(a.index(3))   # 3
print("")


# 集合 Sets
# 用于在一个变量中存储多个项
# 是无序、没有索引的
# 不能包含重复项
# 集合中的项可以增删
# 可以包含任意类型的数据，包括混合数据
# 使用 {} 或 set() 构造集合
a = {1, 2, "three", True}
a = set((1, 2, "three", True))

# 访问集合中的项
# 由于没有索引，我们可以使用循环：
a = {1, 2, 3, 4, 5}
for setItem in a:
    print(setItem)
# 或者可以检查一个特定的项目是否存在：
a = {"Python", "PHP", "Java"}
if "Java" in a:
    print("yes")
print("")

# 添加项
# 使用 add() 方法添加项
a = {"Python", "PHP", "Java"}
a.add("JavaScript")
print(a)   # {'Javascript', 'PHP', 'Python', 'Java'}
print("")

# 从另一个集合中更新集合
# 使用 update() 方法来讲一个集合添加到另一个集合
a = {"Python","PHP","Java"}
b = {"C","C++","C#"}
a.update(b)
print(a)  # {'Python', 'C#', 'C', 'Java', 'PHP', 'C++'}
# update() 也适用于任何可迭代对象
a = {"Python","PHP","Java"}
b = ["c","c++","c#"]
a.update(b)
print(a)  # {'Python', 'C#', 'C', 'Java', 'PHP', 'C++'}
print("")

# 移除/丢弃集合
# 使用 remove() 方法移除集合中的项
# 若指定项不存在，则会报错
a = {"Python","PHP","Java"}
a.remove("Java")
print(a)  # {'PHP', 'Python'}
# 或者使用 discard() 方法移除集合中的项
a = {"Python","PHP","Java"}
a.discard("Java")
print(a)  # {'PHP', 'Python'}
print("")

# 集合运算 - union()
# union() 方法返回包含两个集合项的新集合
a = {"x", "y", "z"}
b = {1, 2, 3}
c = a.union(b)
print(c)  # {'y', 1, 2, 3, 'z', 'x'} （集合是无序的，因此每次输出都不一样）

# 集合运算 - intersection()
# intersection() 方法返回只包含两个集合都有的项目的新集合
a = {"Rome","Paris","Edinburgh"}
b = {"Vienna","Berlin","Edinburgh"} 
c = a.intersection(b)
print(c)  # {'Edinburgh'}

# 集合运算 - symmetric_difference_update() 和 symmetric_difference()
# symmetric_difference_update() 方法保留包含两个集合中独有的项（即与只在一个集合中含有的项，与 intersection() 相反）的新集合
a = {"Rome", "Paris", "Edinburgh"}
b = {"Vienna", "Berlin", "Edinburgh"}
a.symmetric_difference_update(b) 
print(a)  # {'Vienna', 'Rome', 'Paris', 'Berlin'} （集合是无序的，因此每次输出都不一样）
# symmetric_difference() 方法则返回上述值
a = {"Rome", "Paris", "Edinburgh"}
b= {"Vienna", "Berlin", "Edinburgh"} 
c = a.symmetric_difference(b) 
print(c) # {'Berlin', 'Vienna', 'Paris', 'Rome'} （集合是无序的，因此每次输出都不一样）
print("")


# 异常 Exceptions
# 当脚本遇到错误时，程序执行通常会停止
# 我们一般会受到错误信息
# 可以使用 try except 块来处理预期的错误并保持程序运行

# 假设一个脚本只包含： print(x)
# 由于 x 未被定义，这将生成一个错误，程序会退出
# 然而，使用 try except 块，我们可以在预期将引发的异常/错误中处理错误
try:
    print(x) # try to print x
except: # what to do if an error occurs
    print("You didn't initialise x")
    x = input("Set x please: ")
# 如果我们预期有多个错误，我们可以添加多个 except 块
# >>> try:
# >>>     client_obj.get_url(url)
# >>> except (URLError, ValueError):
# >>>     client_obj.remove_url(url)
# >>> except SocketTimeout:
# >>>     client_obj.handle_url_timeout(url)
print("")

# 可以使用 else 块包含一些代码，这些代码将在没有引发错误的情况下运行
try:
    print(a) #try to print a
except: #what to do if an error occurs
    print("you didn't initialise y") 
    y = input("set y please:")
else:
    print("All is well, program finished.")
print("")

# finally 块用于整理
# 下面这个程序程序可以在不打开文件对象的情况下继续
# >>> try:
# >>>     f = open("demofile.txt") 
# >>>     try:
# >>>         f.write("Lorum Ipsum") 
# >>>     except:
# >>>         print("Something went wrong when writing to the file")
# >>>     finally:
# >>>         f.close()
# >>> except:
# >>>     print("Something went wrong when opening the file")

# 抛出异常 Raising exceptions
# 可以选择在特定情况下抛出异常
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero.")
# 也可以定义错误类型
x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed.")