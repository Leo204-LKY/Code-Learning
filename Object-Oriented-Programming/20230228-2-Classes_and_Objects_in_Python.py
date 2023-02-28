# Lecture 2.2: Classes & Objects in Python 类和对象

# Python 是关于对象的！ Python is all about objects!
# name.title()
# "john smith".upper()
# motorbikes.append("ducati")

# 类可以很容易的被定义
class Student:
    # 类以关键字 class 开头，后跟类名，以冒号(:)结束
    # 类名字应遵循 Python 变量命名规则

    """A class representing a student"""

    def __init__(self, na, ag):
        self.full_name = na
        self.age = ag
    # 特殊的类方法 __init__() 用于初始化使用该类创建的对象(实例)
    # self - 一个引用正在创建的对象的特殊参数

    def get_age(self):
        return self.age
    # get_age 方法 - 返回年龄属性的值，注意使用 self - 用来引用我们想要返回其值的对象(实例)

john = Student("John Cleese", 78)
# 创建一个 Student 对象，保存在变量 john 中


# Python Classes - The Basics
# 最简单的定义类的形式：
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# 类定义中的语句通常是方法定义，但也允许使用其他语句，有时这些语句还很有用——稍后讨论
# 类定义和函数定义(def语句)一样，必须在它们生效之前执行
#   - 你可以把类定义放在Python if 语句的分支中，或者放在函数中

# __init__ 方法
# - 当我们从类中创建一个新实例时，Python自动运行的特殊方法
# - __init__() 方法的第一个参数必须是 self
#     - 指向当前正在创建的对象
# - 其他参数是用于初始化对象的值
# - 没有 return 语句
# Python 参数并不一定需要 __init__() 方法 - 碰巧它非常有用(Python classes DO NOT REQUIRE an __init__() method - just so happens that it is very useful!)
# 这个方法名称前后各有两个下划线，这是一个有助于防止 Python 的默认方法名称与您的方法名称冲突的约定
# 一个类中没有 __init__() ，包含一个参数的 __init__() 和包含个参数的 __init__() 都是有效的