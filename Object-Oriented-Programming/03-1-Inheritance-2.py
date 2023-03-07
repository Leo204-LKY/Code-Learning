# Lecture 3.1: Inheritance in Python 继承 Part 2

# Dealing with a Variable Number of Arguments 处理可变数量的参数
# 在某些情况下，我们需要函数对不同数量的参数进行操作
# Python 支持使用 *args 和 *kwargs 来实现
# - *args 允许我们指定一个函数(或方法)可以有不同数量的位置参数
# - **kwargs 允许我们指定一个函数(或方法)可以有不同数量的关键字参数(或命名参数，如 ma = "Audi")
def my_sum(*args):
    result = 0
    # Iterating over the python args tuple
    for x in args:
        result += x
    return result


# Multiple Inheritance 多重继承
# Python 中一个类支持从多个父类中继承
# 格式：
# >>> class <classname>(<superclassName1>,<superclassName2>,...):
class Car:
    __doc__ = 'Car Class'

    """Class attribute to hold list of Cars created."""
    all_cars = []

    def __init__(self, ma, mo, yr, **kwargs):
        super().__init__(**kwargs)
        self._make = ma
        self._model = mo
        self._year = yr
        """_odometer_reading should only be accessed/modified via internal methods"""
        self.__odometer_reading = 0
        Car.all_cars.append(self)
    # ... OTHER CODE HERE

class Boat:
    __doc__ = 'Simple Boat Class'
    
    """Represent boat characteristics."""
    
    def __init__(self, dis, blst, **kwargs):
        super().__init__(**kwargs)
        self._displacement = dis
        self._ballast = blst
    # ... OTHER CODE HERE

class AmphibiousVehicle(Car, Boat):
    """Represent amphibious vehicle - using multiple inh.""" 

    def __init__(self, fp, **kwargs): 
        """Initialize attributes of the parent classes.""" 
        super().__init__(**kwargs)
        """Initialize attrs for amphibious vehicle."""
        self._snorkel = False
        self._folding_prop = fp
    
    def convert(self):
        if self._folding_prop:
            print('Waiting for propeller ...')
            print('Preparing to sail ...')

car1 = Car(ma='Audi',mo='Q7',yr=2004)
boat1 = Boat(dis=200,blst=True)
amph1 = AmphibiousVehicle(ma='VW',mo='Schwimmwagen',yr=1944,fp=True,dis=900,blst=True)
