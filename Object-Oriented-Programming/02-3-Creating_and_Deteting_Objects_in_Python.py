# Lecture 2.3: Creating & Deleting Objects in Python 创建 & 删除对象

# Constructors & Initializers 构造函数和初始化函数
# 大多数面向对象编程语言都有构造函数的概念，构造函数是一种特殊的方法，在创建对象时创建并初始化对象
# Python略有不同——它有一个构造函数 __init__() 和一个初始化函数 __new__()

# __new__() 函数只接受一个参数——正在创建的类，并返回最新创建的对象
# 很少使用，除非你在做一些奇异的事情——在日常编程中不是很有用!

# 从类中创建一个实例很简单：调用类名，后跟圆括号
# >>> my_car = Car("Audi", "Q5", 2007)
# >>> print(my_car)  # <__main__.Car object at 0x7fca2fa90c88>
# >>> hm_car = Car("Bentley", "Mulsanne", 2017)
# >>> print(hm_car)  # <__main__.Car object at 0x7ff30e5a1da0>
# print 的结果告诉我们这些是 Car 类的对象和它们的内存地址。注意不同的地址，即两个不同的对象

# 删除对象
# 许多面向对象语言要求类具有显式的 destructor 方法
# - 说明当一个对象不再需要时该做什么
# - 通常恢复/释放该对象使用的内存。
# Python 的“垃圾处理”则是自动的，它会会自动检测对一段内存的所有引用何时超出作用域(gone out of scope)，并自动释放内存。
# 通常工作良好，很少有内存泄漏。

# gc 模块(module)
# 暴露Python的底层内存管理机制，自动垃圾收集器。 gc 模块包括用于控制收集器如何操作和检查系统已知对象的函数，这些对象要么是挂起的收集，要么是卡在引用循环中无法释放的。

# Python类可以定义 __del__(self) 方法，该方法在实例即将被销毁时被调用(多数时候用不上！)