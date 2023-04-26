# Lecture 11.4: *Decorator* Pattern 修饰器模式  

| 模式 | Decorator 修饰器（也称 Wrapper） |
| --- | --- |
| 递归（Recurring）问题 | 当子类化（subclassing）不切实际时，如何动态地为对象增加新的职责？ |
| 解决方案 | 1. 实现一个或多个装饰器类<br>2. 将一个对象封装在具有类似接口的装饰器对象中 |
| 结果 | 可以在运行时添加/删除行为<br>避免子类爆炸 |

## GoF 版本的修饰器  
![GoF Version of Decorator](https://user-images.githubusercontent.com/57821066/234462912-88c60eac-d96e-4b88-bc2d-4e9088ece447.png)  

## 修饰器模式 & Python  
考虑这个例子：  
```Python
class Car:
    ...
    def assemble(self):
        pass

class BasicCar(Car):
    ...
    def assemble(self):
        print("Basic Car."")
```
如果我们想为从 `BasicCar` 创建的对象包括额外的行为，比如跑车选项和豪华车选项，该怎么办？  
- 可以创建 `BasicCar` 的子类…
    ```Python
    class CarDecorator(Car):
        def __init__(self, car):
            self.car = car

        def assemble(self):
            self.car.assemble()

    class SportsCar(CarDecorator):
        def __init__(self, car):
            super().__init__(car)

        def assemble(self):
            super().assemble()
            print("Adding features of Sports Car.")

    class LuxuryCar(CarDecorator):
        def __init__(self, car):
            super().__init__(car)

        def assemble(self):
            super().assemble()
            print("Adding features of Luxury Car.")
    ```
    ```
    >>> sports_car = SportsCar(BasicCar())
    >>> sports_car.assemble()
    >>>
    Basic Car.
    Adding features of Sports Car.
    >>> sports_luxury_car = SportsCar(LuxuryCar(BasicCar()))
    >>> sports_luxury_car.assemble()
    Basic Car. 
    Adding features of Luxury Car. 
    Adding features of Sports Car.
    ```
- 或者使用修饰器模式  

## Python 中的修饰器  
- Python 有它自己的 *decorators* 修饰器 - 与 GoF 的修饰器模式不同  
    - Python 中的修饰器是任何可调用的 Python 对象，用于修改函数或类  
    - 对函数 `func` 或类 `C` 的引用被传递给修饰器，修饰器返回修改后的函数或类  
    - 修饰器的符号是 `@`
```Python
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))
```
```
>>> foo(‘Hi’)
Hi, foo has been called with Hi
>>> foo = our_decorator(foo)
>>> foo(42)
Before calling foo
Hi, foo has been called with 42
After calling foo
```
使用修饰器 `@` 可以改写为  
```Python
def our_decorator(func):
    ... # As above ...

@our_decorator
def foo(x):
    print("Hi, foo has been calles with " + str(x))
```