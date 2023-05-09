# Lecture 12.1: *Strategy* Pattern 策略模式  

| 模式 | Strategy 策略（也称 Policy） |
| --- | --- |
| 递归（Recurring）问题 | 如何组织相关的算法(行为)并使一个类可以配置其中的一个？ |
| 解决方案 | 1. 创建一个抽象策略类(或接口)，并以多种方式扩展(或实现)它<br>2. 每个子类以不同的方式定义相同的方法名 |
| 结果 | 为重用而组织的相关算法或行为族<br>提供实现的选择<br>消除了许多条件语句 |

## GoF 版本的策略  
![GoF Version of Strategy](https://user-images.githubusercontent.com/57821066/237018637-1b3610a1-7117-401c-9880-1aa61987854b.png)  

## 策略模式 & Python  
考虑以下例子：  
```Python
from abc import ABC

class Strategy(ABC):
    def check_temperature(self, temperature):
        pass

class HikeStrategy(Strategy):
    def check_temperature(self, temperature):
        if temperature >= 16 and temperature <= 30:
            return True
        else:
            return False

class SkiStrategy(Strategy):
    def check_temperature(self, temperature):
        if temperature <= 0:
            return True
        else:
            return False

class Context:
    def __init__(self, temperature, strategy):
        self.temperature = temperature
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_temperature(self):
        return self.temperature

    def get_result(self):
        return self.strategy.check_temperature(temperature)
```
```
>>> temperature = 20
>>> strategy_ski = SkiStrategy()
>>> context = Context(temperature, strategy_ski)
>>> print('Is the temperature ({} C) good for skiing? {}'.format(context.get_temperature(), context.get_result()))
Is the temperature (20 C) good for skiing? False

>>> strategy_hike = HikeStrategy()
>>> context.set_strategy(strategy_hike)
>>> print(‘Is the temperature ({} C) good for hiking? {}’.format(context.get_temperature(), context.get_result()))
Is the temperature (20 C) good for hiking? True
```