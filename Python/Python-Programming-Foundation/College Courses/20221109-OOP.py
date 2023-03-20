# Object orientated programming (OOP)
# 面向对象程序设计

# OOP 是一种编程范式(“风格/方法/做事方式”等)
# OOP 在各种不同的语言中都得到支持
# 从本质上说， OOP 是一种方法，通过它我们可以对问题和解决方案进行高度抽象的建模

# Steve Jobs 的解释
# 物体就像人。它们是有生命的，会呼吸的生物，体内有如何做事的知识，体内有记忆，所以它们能记住事情。而不是在一个非常低的层次上与它们交互，你在一个非常高的抽象层次上与它们交互，就像我们在这里做的一样。
# 举个例子:如果我是你的洗衣对象，你可以把你的脏衣服给我，然后给我发一条信息说:“你能帮我把衣服洗一下吗?”我碰巧知道旧金山最好的洗衣店在哪里。我说英语，我口袋里有钱。所以我出去叫了一辆出租车，让司机带我去旧金山的一个地方。我去把你的衣服洗了，然后跳回出租车，回到这里。我把你的干净衣服给你，说:“这是你的干净衣服。”
# 你不知道我是怎么做到的。你对洗衣房一无所知。也许你会说法语，但你甚至不会叫出租车。你没钱买，你口袋里没钱。但我知道怎么做所有这些。你根本不需要知道这些。所有的复杂性都隐藏在我的内心，我们能够在一个非常抽象的高度进行互动。这就是对象。它们封装了复杂性，与该复杂性的接口是高级别的。
# Translated by Youdao from English.

# 三个重要的语言特性
# 抽象数据类型
  # 数据抽象
  # 封装
  # 信息隐藏
# 继承
# 多态性

# The Zen of OOP
# Whenever you can clearly separate data and associated tasks within a computation, you should do so (Sedgewick, Wayne, Dondero (2015)
# 只要你能清楚地在计算中区分数据和相关任务，你就应该这样做

# 对象(object)、类(class)和构造函数(constructor)
# - 对象通过类来创建
# - 类用于表示对象的类型
# - 构造函数是用于创建对象的类
# - 出于所有的意图和目的，我们认为对象和类相同
# - 每个类都需要一个构造函数
#   - 构造函数用于创建类
#   - 我们可以自行创建
#   - 若不自行创建， Python 会为类创建一个默认的构造函数

# 创建对象
# Python 中的所有内容都是对象

# 创建类
# 用 class 来创建类别
# Define
class Cat:
    name = "Cortex"
    age = 10
# Create
cat1 = Cat()
# Access properties
print(cat1.age)

# 所有的对象都包含 __init__()（初始化的缩写）
# __init__() 函数会在对象创建时自动调用
# self 类似其他函数中的 this ，指的是特定对象的当前实例
# __init__() 方法的第一个参数必须是 self ，表示创建的类实例本身，因此，在 __init__ 方法内部，就可以把各种属性绑定到 self ，因为 self 就指向创建的实例本身。
# 有了 __init__ 方法，在创建实例的时候，就不能传入空的参数了，必须传入与 __init__ 方法匹配的参数，但 self 不需要传， Python 解释器会自己把实例变量传进去：
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Cortex", 10)
print(cat1.name) 
print(cat1.age)

# Class methods 类方法
class Robot:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def sayName(self):
        print("I am "+ self.name)
    
myRobot = Robot("Nao", "Blue")
myRobot.sayName()
# 这里的 sayName() 就是一个方法

# 访问类属性
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

myCar = Car("Mini", 100) # 创建

print(myCar.name)        # 访问

# 修改类属性
myCar.name = "Mini one"
print(myCar.name)

# 删除类属性
del myCar.speed
# >>> print(myCar.speed)  # Attribute error

# 删除类
del myCar
# >>> print(myCar.name)   # NameError: name 'myCar' is not defined

# Inheritance 继承
# OOP 的一个重要特性
# 继承为一个对象从另一个对象继承方法和属性提供了一种方法，例如 ACar 对象从 Vehicle 对象继承了 Drive 函数
# 继承有助于代码的重复利用
# 当我们想到继承时，我们通常指的是
# - 父类(包含适用于多个对象的通用属性和方法)
# - 子类(父类的子类，继承父类的属性和方法)
# e.g.
# Polygon 有两个属性和两个方法
class Polygon:  # 多边形
    def __init__(self, n_sides):
        self.n_sides = n_sides
        self.l_sides = [0 for i in range(n_sides)]

    def setSideLength(self):
        self.l_sides = [float(input("Enter length of side " + str(i + 1) + " : ")) for i in range(self.n_sides)]
    
    def viewSides(self):
        for i in range(self.n_sides):
            print("Side", i + 1 , "is", self.l_sides[i])

# 我们可以创建一个 Square 类来继承 Polygon 中的所有属性和方法
class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)
# Square 可以调用 setSideLength 和 viewSides ，尽管后两者未在 Square 类中被定义

# 我们也可以使用 super() 函数替换父类名，子类将自动继承父类的属性和方法
class Square(Polygon): 
    def __init__(self):
        super().__init__(4)

s = Square()
s.setSideLength()
s.viewSides()
print(isinstance(s,Square))

# 方法(methods)与函数(functions)
# 方法与对象有联系，函数没有
# 方法不能用名字调用，函数可以


# Polymorphic classes 多态类
# 多态性允许我们创建对象，其中包含与不同对象中的方法同名的方法
#具有相似属性的不同对象可能具有相似的行为、操作等方法
# 我们认为多态有多种形式
class Italy():
    def capital(self):
        print("Rome")
    def language(self):
        print("Italian")
    def currency(self):
        print("Euro")

class Scotland():
    def capital(self): 
        print("Edinburgh")
    def language(self):
        print("English") 
    def currency(self):
        print("Pound")
# Italy 和 Scotland 两个类中各有相似的结构和相同名字的方法
# 它们都没有超级类(Super class)或父类(Parent)
# 我们可以类似地使用这两个对象，而不管它们的类型不同
# 我们可以在不引用任何对象的类名的情况下做到这一点
i = Italy()
s = Scotland()

for country in (i, s):
    country.capital()
    country.language()
    country.currency()

print(type(i))
print(type(s))
print(isinstance(s, Italy))
print(isinstance(i, Scotland))
# 这两项都有相同名称的类方法，因此调用时不需要关心对象类型/类类型

# Multiple inheritance 多重继承
# 单个类具有多个父类
class Staff:
    def __init__ (self, name, uid):
        self.name = name 
        self.uid = uid

class Employee:
    def __init__ (self, role, salary): 
        self.role = role 
        self.salary = salary

class Secretary(Staff, Employee):
    def __init__ (self, name, uid, role, salary, exp): 
        self.exp = exp
        Staff.__init__(self, name, uid) 
        Employee.__init__(self, role, salary)
    def basicInfo(self):
        print({self.name, self.role, self.exp})
# Secretary 从 Staff 和 Employee 继承了内容
    
s = Secretary("Beth", "b289", "Admin", 1000, 5) 
s.basicInfo()

# Encapsulation 封装
# 一个对象变量不应该总是可以直接访问的，为了避免错误修改，我们可以将对象变量设为私有
# 在变量前加入双下划线__即可
# 其他编程语言使用 Python 中不可用的访问修饰符
class User:
    def __init__(self):
        self.name = "JP"
        self.__password = "secret"

u = User()
# >>> print(u.password)
# AttributeError: 'User' object has no attribute 'password'
# >>> print(u.__password)
# AttributeErrorL 'User' object has no attribute '__password'

# 使用 getter 和 setter 方法来修改私有变量
# Getter和setter方法可用于包含额外的检查，以确保在访问或修改私有变量时遵守某些标准
class User:
    def __init__(self):
        self.name = "JP"
        self.__password = "secret"
    
    def getPassword(self):
        print(self.__password)
    
    def setPassword(self, newPassword):
        self.__password = newPassword

u = User()
u.getPassword()
u.setPassword("New Secret")
u.getPassword()

# 小结
# OOP 的内容比这里介绍的多得多
# OOP 主要涉及设计
#   - 识别物体
#   - 理解对象属性
#   - 理解对象之间的关系
#   - 了解对象之间的相互作用
# 以后将会学到更多关于 OOP 和其他范例的知识