# 编程步骤(第3讲)：
# 需求分析、程序设计、代码编写、测试与调试、实施与开发、维护优化


# Python 的基础语法

# 1. 标识符
# 程序开发过程中自定义的一些符号和命名，具有以下特点：
# 不能用数字开头： 1x = 1 是错误的
# 可由字母、数字、下划线组成：hello_1 是可以的
# 区分大小写：a、A 是两个不同的变量
#
# 命名法则：
# 避开 Python 自身关键词：False、True、None、and、as、assert、break、class、continue、def、del、elif等
# 下划线命名法(Python 中常用)：lower_to_upper
# 驼峰命名法： myPython
# 
# 行与缩进
# Python 使用缩进代表代码块(Block)（Python 的一大特色，有的编程语言使用{}等代表代码块）
# 每个代码块的缩进必须相同，否则程序会认为是两个不同代码块，会报错
# 
# 常见错误：
# 全角/半角符号不分：if a < b：
#                           ^中文冒号不可以
# 缺少符号，如只有前括号
# 溢出问题(2.i. 中介绍)

# 2. 数据类型
# 赋值
# 使用“=”进行赋值
# “=”代表赋值，“==”代表相等
# 
# 6 种数据类型：数字、字符串、列表、元组、集合、字典
# 
# i. 数字
# 整数(int)：如 2、3、-1等
# 浮点数(float)：如 2.5、3.2 等
# 复数(complex) ：由实数和虚数组成
# 这三种数都有一定范围，超出范围会报错
# 
# 溢出问题：
# 例：计算 44 + 0.158061 <- 整数与浮点数相加
# 输出： 44.158061000000004 <- 超出计算机所能使用的数据的一个表达范围，产生溢出
# 
# ii. 字符串/串(String)
# 是由数字、字母、下划线等组成的一串字符，由单引号或双引号来创建：'asd'、'123'、'k%5'、"How are you"等
# * 单引号和双引号在 Python 中几乎没有区别，但当创建字符串时使用了单引号，字符串内的引号就应该用双引号
#   也可使用“\”来转义，如"Simon says: \"Sit down\"."
#   使用三引号可实现跨行赋值（单引号和双引号均可）
#   例：'''hello
#       python'''
#   输出：'hello\npython'
# 两个字符串可用“+”号连接：'hello' + 'how are you' = 'hellohow are you'
# 
# 在给字符串赋值时，实际上也给字符串中的字母拍好了次序
# 第一个字母对应位置是0、第二个是1…最后一个是-1
# 当需要提取字符串中的部分内容时，可以用位置信息进行提取
# 例：x = "Python"
# x[1] = 'y'
# x[-2] = 'o'
# 
# iii. 列表
# 一种有限的有序值的集合，用方括号表示：x = [1,2,3]
# 列表中的元素类型可以不同：[1, 'text', 3.14]
# 列表中每个元素都有一个索引值，从 0 开始 