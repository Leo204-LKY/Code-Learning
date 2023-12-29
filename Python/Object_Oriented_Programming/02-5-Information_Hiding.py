# Lecture 2.5: Information Hiding 信息隐藏

# 大多数面向对象编程语言都有访问控制的概念
# - 这与抽象有关。
# - e.g. Java有关键字 public, protected 和 private ——用来控制数据成员和方法的可见性
#   - Private - 只能在类的实例中访问
#   - Protected - 仅在类及其任何子类的实例中访问
#   - Public - 允许访问任何对象
# 注意： Python 不是这样

# Python 的所有属性和方法都是公共的
# 可以通过插入文档字符串并在名称前加上单下划线(_)，来建议某个属性或方法不应该被公开访问
class Car:
    def __init__(self, ma, mo, yr):
        self.make = ma
        self.model = mo
        self.year = yr
        self._odometer_reading = 0
    """_odometer_reading should only be accessed/modified via internal methods"""
    # ...

# Name Mangling 名称重整/名称改编
# - 模拟私有属性和方法 Simulates private attributes and methods.
# - 名称前带有双下划线(__)且尾下划线不超过一个
# - 仍然可以被外部对象访问(如果真的有必要)，但需要额外的工作
#   - Name Mangling 不保证隐私，它只是强烈建议 Name mangling does not guarantee privacy, it only strongly recommends it!\
class Car:
    def __init__(self, ma, mo, yr):
        self._make = ma
        self._model = mo
        self._year = yr
        self.__odometer_reading = 0
    # ...

my_car = Car("Audi", "Q7", 2016)

my_car._make
# >>> Audi
my_car.__odometer_reading
# >>> AttributeError: 'Car' object has no attribute '__odometer_reading'
# 如果需要在外部访问，在前面加上 _<classname>
my_car._Car__odometer_reading
# >>> 0


# Accessing Unknown Members
# 偶尔，类的属性或方法的名称只在运行时给出…
# Python 提供了内置函数来帮助： getattr(), setattr(), hasattr()
# getattr(object_instance, string)
#   - string 是包含类的属性名或方法名的字符串
#   - 返回对该属性或方法的引用
# hasattr(object_instance, string)
#   - 如果对象具有属性或方法名匹配字符串，则返回 True
# setattr(object_instance, string, value)
#   - 将值赋给属性
my_car = Car('Audi', 'Q7', 2016)
getattr(my_car, '_make')
# >>> Audi
getattr(my_car,'get_fullname')
# >>> <bound method Car.get_fullname of <__main__.Car object at 0x7f008796c7f0>>
getattr(my_car,'get_fullname')()
# >>> Audi Q7
hasattr(my_car,'engine_size')
# >>> False


# Build-In Members of Classes 类的内置成员
# 类包含许多Python包含的方法和属性，即使你没有显式地定义它们
# 所有内置 members 的名称前后都有双下划线
#   e.g. __init__()  __doc__

# 特殊数据项 Data Items
# __doc__ - 类的文档字符串，如果未定义则为None
# __name__ - 类名称
# __dict__ - 包含类名称空间的字典
# __module__ - 定义类的模块名

# 特殊方法 Methods
# __init__() - 类的初始化式
# __repr__() - 定义如何计算对象的“正式”字符串表示。应该是一个有效的Python表达式，可以重新创建对象
# __str__ - 指定如何将类的实例转换为“非正式的”可打印的字符串表示形式
# __len__() - 定义 len(obj) 的工作方式
# __eq__() - 定义==对对象的行为

# 强化版的 Car 类例子...
class Car:
    __doc__ = "Luxury Car Class"

    """Class attribute to hold list of Cars created."""
    all_cars = []

    def __init__(self, ma, mo, yr):
        self._make = ma
        self._model = mo
        self._year = yr
        """__odometer_reading should only be accessed/modified via internal methods"""
        self.__odometer_reading = 0
        Car.all_cars.append(self)

    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())
    
    def __str__(self):
        return "Car: " + self.get_fullname()
    
    def __len__(self):
        return self.get_car_age()
    
    def __eq__(self, other):
        return (self._make == other._make and self._model == other._model)
    
    def get_fullname(self):
        """Return a neatly formatted descriptive name.""" 
        long_name = str(self._year) + ', ' + self._make + ' ' + self._model
        return long_name.title()
    
    def get_car_age(self, current_year=2017): 
        """Return the age of the car in years."""
        return current_year - self._year
    
    def increment_odometer(self, miles): 
        self.__odometer_reading += miles
