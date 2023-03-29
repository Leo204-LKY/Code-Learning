# Lecture 3.3: Names, Modules & Monkeys 名称、模块和猴子(补丁)

# Namespaces 命名空间
# - 名称到对象的映射
#   - 使用Python字典实现
# - 示例
#   - 内置名称集(abs() 等)
#   - 模块内定义的全局名称
#   - 函数中的局部名称
#   - 对象内的属性
# 不同名称空间中的名称之间没有关系。例如，两个不同的模块都可以定义一个函数 foo() 而不会混淆 - 模块的用户必须在函数 foo() 前加上模块名
# 了解名称空间对于理解Python如何搜索名称非常重要：
# Build-in names 内置名称
#  ⌞ Current module's global names 当前模块的全局名称
#     ⌞ Enclosing function n 封闭函数 n
#        ⌞ Enclosing function 1 封闭函数 1
#           ⌞ Innermost level (local names) 最内层(本地名称)


# Modules in Python 模块
# 模块帮助组织程序
# - 一旦代码超越了几个类/函数，就变得至关重要
# 模块就是简单的Python文件(扩展名为.py)
# - 在同一个文件夹中有两个或多个文件 - 可以从一个模块中加载类/函数以在其他模块中使用
# import - 用于导入模块、类或函数的语句
# 不同版本的 import
# >>> import <somefile>
# >>> from <somefile> import <className/functionName>
# >>> from <somefile> import <className/functionName> as <alias>
# >>> from <somefile> import *
# 区别：从模块中导入的内容以及导入后引用它的名称
# Python在 sys.path 寻找模块
# - 保存文件夹列表的变量。
# 程序可以修改 sys.path: sys.path.append("/my/new/path")

# 一些例子 - 在 students.py 中导入
import database
db = database.Database()
# 将数据库模块导入 student 名称空间

from database import Database
db = Database()
# Do queries on db 在 db 上执行查询
# 将 Database 类从数据库模块导入到 student 名称空间

from database import Database as DB
db = DB()
# Do queries on db
# 将 Database 类从数据库模块导入到 student 命名空间，名称为 DB

from database import *
db = Database()
# Do queries on db
# 将数据库模块中的所有类和函数导入 student 命名空间
'''注意：不要使用第四种方法。每个有经验的Python程序员都会告诉你，永远不要使用这种语法。使代码无法管理和维护'''


# Organising Modules 组织模块
# 当项目成长为模块的集合时，可能需要添加另一个抽象级别：package 包 - 文件夹中的模块集合
# __init__.py 文件 - 使 Python 将文件夹视为包所必要的文件。最简单的情况是， __init__.py 可以是一个空文件

# 一个包的例子
'''
game/               # top-level package 顶级包 
    __init__.py
    characters/     # 初始化游戏包，游戏角色及其行为的子包
        __init__.py
        pacman.py
        ghosts.py
        ...
    items/          # 游戏道具(非角色)的子包
        __init__.py
        dots.py
        power_pellets.py
        ...
    maze/           # 迷宫和相关功能的子包
        __init__.py
        build_maze.py
        solver.py
        ...
'''
# >>> import game.maze.build_maze
# >>> game.maze.build_maze.draw(...)


# Monkey Patching 猴子补丁
# 类或模块在运行时的动态修改
# 什么时候用它？
# - 当且仅当一个问题没有其他解决方案时
# - 会导致不可预测的行为
# - 典型情况：
#   - 解决第三方代码中的错误
#   - 适应标准模块
#   - 代码插装
#   - 测试

# 一个简单的示例：
# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> math.pi = 3
# >>> math.pi
# 3

# def safe_sqrt(num):
#   # doesn't throw exception if num < 0
#   if num < 0:
#       return math.nan
#   return math.original(num)
# >>> import math
# >>> math.original = math.sqrt
# >>> math.sqrt = safe_sqrt


# Python Enhacement Proposal #8 (8 号 Python 增强规范，PEP-8)
# PEP-8 风格的 Python 代码指南
'''“代码被阅读的次数比被编写的次数要多。这里提供的准则旨在提高代码的可读性，并使其在广泛的Python代码中保持一致。”'''