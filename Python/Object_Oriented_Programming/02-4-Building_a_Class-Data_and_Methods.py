# Lecture 2.4: Building a Class - Data & Methods 创建类 - 数据和方法

# Data attributes 数据属性
# - 类的特定实例所拥有的变量。
# - 最常见的属性。
# - 可以在类定义中使用 __init__() 进行初始化，或者可以在对象创建后设置任意数据属性
class Car:
    def __init__(self, ma, mo, yr):
        self.make = ma
        self.model = mo
        self.year = yr
        self.odometer_reading = 0 # 这里我们为未传递给 __init__() 的属性设置默认值

# 用 <object>.<attribute> = <value> 语法来为对象的属性赋值(dot notation 点记法)
my_car = Car("Audi", "Q7", 2016)

my_car.odometer_reading = 10000
my_car.fuel = "diesel"
# 这个对象现在有 make, model, year, odometer_reading 和 fuel 五个参数

# Methods 方法
# 包含在类中的函数称为方法(格式与函数相同)
# 方法与普通函数的区别在于，所有方法都有一个必需的参数 self
# - 虽然在定义方法时必须显式指定 self ，但在调用方法时不用包括它 - Python会自动为你传递
class Car:
    def __init__(self, ma, mo, yr):
        self.make = ma
        self.model = mo
        self.year = yr
        self.odometer_reading = 0
    
    def get_fullname(self):
        """"Return a neatly formatted descriptive name."""
        long_name = self.make + " " + self.model
        return long_name.title()
    
    def get_car_age(self, current_year = 2023):
        """Return the age of the car in years."""
        return current_year - self.year

my_car = Car("Audi", "Q7", 2016)
my_car.get_fullname() # Audi Q7
my_car.get_car_age()  # 7


# Revisiting self
# 类中每个方法的第一个参数是对类(对象)当前实例的引用
# 按照惯例，我们将这个参数命名为 self
# - 在 __init__() 中， self 指向当前正在创建的对象
# - 在其他方法中，它引用被调用方法的实例
# 与 Java 或 C++ 中的 this 关键字类似
# 约定使用 self 作为名字，但是使用 this 或者甚至 Martha 也是可以的


# Class Attributes 类属性
# - 由整个类拥有 Owned by the class as a whole.
# - 在类定义中定义，在任何方法之外定义 Are defined within a class definition and outside of any method.
# - 所有类实例共享它的相同值
# - 在某些语言中称为 static(静态) 变量
# - 适用于：
#   1. class-wide 常数
#   2. 计算一个类已经创建了多少实例
class Car:
    all_cars = []
    # all_cars 是类定义的一个列表部分——因此由 Car 类的所有实例共享

    def __init__(self, ma, mo, yr):
        self.make = ma
        self.model = mo
        self.year = yr
        self.odometer_reading = 0
        Car.all_cars.append(self)
        # 创建的每个Car对象都被添加到 all_cars 列表中

# 使用 <classname>.<attribute> 或 <object>.__class__.<attribute> 来访问一个类属性
my_car = Car("Audi", "Q7", 2016)
yo_car = Car("Land Rover", "Disco", 2014)
print(Car.all_cars)               # [<__main__.Car object at 0x7fa797922fd0>, <__main__.Car object at 0x7fa797922ef0>]
print(my_car.__class__.all_cars)  # [<__main__.Car object at 0x7fa797922fd0>, <__main__.Car object at 0x7fa797922ef0>]

# Python 也同时支持类方法 class methods - 操作类而不是实例的方法/即不需要实例化类就可以直接访问使用的方法
# 使用函数修饰器(decorators):
# @classmethod   - 方法对类进行操作，但不传递self，而是传递类(cls)
# @ staticmethod - 方法对类进行操作，但不传递self，也不传递类(cls)
class Car:
    # ...
    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())
    # ...

Car.print_inventory()
# >>> Audi Q7
# >>> Land Rover Disco

class Student:
    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(" ")
        return len(names) > 1

Student.is_full_name("Bob")        # False
Student.is_full_name("Bob Smith")  # True


# 目前为止的 Car 类例子...
class Car:
    """Class attribute to hold list of Cars created."""
    all_cars = []
    def __init__(self, ma, mo, yr):
        self.make = ma
        self.model = mo
        self.year = yr
        self.odometer_reading = 0
        Car.all_cars.append(self)

    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())

    def get_fullname(self):
        """Return a neatly formatted descriptive name.""" 
        long_name = str(self.year) + ', ' + self.make + ' ' + self.model
        return long_name.title()
    
    def get_car_age(self, current_year=2017): 
        """Return the age of the car in years."""
        return current_year - self.year
    
    def increment_odometer(self, miles): 
        self.odometer_reading += miles
