# Lecture 2.6: Inheritance in Python 继承 Part 1

# 我们在 Python 中创建的每个类都使用继承 - 它们都是 object 的子类
# class Car: ... 即 class Car(object): ...

# 一个类可以扩展另一个类的定义 - 允许使用(或扩展)超类(或父类，superclass)中已经定义的方法和属性
# 继承的语法：class <classname>(<superclassName>):
class ElectricCar(Car): # Car 类详见 Lecture 2.5
    """Represent aspects specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # 注意这里调用父类__init__()方法。
        self._max_range = 300
        # _max_range 是 ElectricCar 独有的一个新属性
    # ...

my_car = Car("Audi", "Q7", 2016)
el_car = ElectricCar("Tesla", "Model S", 2017)
print(el_car)
# >>> Car: 2017, Tesla Model S
el_car._max_range
# >>> 300
my_car._max_range
# >>> AttributeError: 'Car' object has no attribute ‘_max_range'

# 一旦我们有了继承自父类的子类，我们就可以添加任何必要的新属性和方法来区分子类和父类
# 但请记住：不特定于子类的属性或方法应该添加到超类而不是子类中
class ElectricCar(Car):
    """Represent aspects specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. """
        super().__init__(make, model, year)
        """Initialize attributes specific to an electric car."""
        self._max_range = 300
        self.__battery_level = 100

    def report_battery(self):
        """ Report private attribute holding battery level."""
        print(self.__battery_level)
    
    def charge_battery(self):
        """ Increase __battery_level as charging."""
        if self.__battery_level < 100:
            self.__battery_level +=1
        else:
            print('Danger - overcharging!')

# Overriding 覆写/重写
# 要重写从超类继承的方法：在子类中定义一个方法，与你想从超类中重写的方法同名 - Python 将完成其余的工作


# super()
# Python 的 super() 函数提供了一种强大的机制——允许子类调用其超类中的方法代码
# super() 计算对超类的引用，而无需程序员显式地命名该类
# 单继承场景：实现灵活、可维护的代码

# Example 1
class ElectricCar(Car):
    """Represent aspects specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. """
        super().__init__(make, model, year)
        """Initialize attrs specific to an electric car."""
        self._max_range = 300
        self.__battery_level = 100
    # ...

# Example 2
class ElectricCar(Car):
    def get_fullname(self):
        """Return a high voltage descriptive name.""" 
        long_name = "**" + str(self._year) + ", " + self._make + " " + self._model + "**"
        return long_name.title()
    # get_fullname() in ElectricCar class

    def get_fullname(self):
        """Return a high voltage descriptive name.""" 
        long_name = "**" + super().get_fullname() + "**"
        return long_name.title()
    # get_fullname() in ElectricCar using super() to call get_fullname() in Car class

# Car 和 ElectricCar 类的例子
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
        
class ElectricCar(Car):
    """Represent aspects specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. """
        super().__init__(make, model, year)
        """Initialize attributes specific to an electric car."""
        self._max_range = 300
        self.__battery_level = 100
    
    def report_battery(self):
        """Report private attribute holding battery level."""
        print(self.__battery_level)
    
    def charge_battery(self):
        """Increase __battery_level as charging."""
        if self.__battery_level < 100:
            self.__battery_level +=1
        else:
            print("Danger - overcharging!")
    
    def get_fullname(self):
        """Return a high voltage descriptive name.""" 
        long_name = "**" + super().get_fullname() + "**"
        return long_name.title()