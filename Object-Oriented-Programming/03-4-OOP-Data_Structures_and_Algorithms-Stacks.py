# Lecture 3.4: Object-Oriented Programming: Data Structures and Algorithms: Stacks 面向对象编程 - 数据结构和算法：堆栈

# Stack 堆栈
# Data Structures and Algorithms 数据结构和算法
# - Goodrich Book: Chapter 6 - Data Structures and Algorithms in Python, 2013, Wiley, by Michael Goodrich (in the library as an ebook) 
# 为什么需要它
# - 更高效、简单地解决问题
# - 想象一下在 Word 中“撤销”和“重做”操作是如何实现的
# 本讲将介绍 Stack 堆栈


# Abstract Data Types (抽象数据类型，ADTs)
# ADT 是数据结构的抽象
# ADT规定:
# - 已存储的数据
# - 对数据的操作
# - 操作相关的错误情况
'''
示例：ADT 建模一个简单的股票交易系统
- 存储的数据为买入/卖出订单
- 支持的操作为
  - 订单买入(客户，股票，股票，价格)
  - 订单卖出(客户，股票，股票，价格)
  - 无效取消(订单)
-错误条件
  - 买入/卖出不存在的库存
  - 取消不存在的订单
  - 订单没有关联客户
'''


# The Stack ADT 堆栈 ADT
# 堆栈ADT存储任意对象
# - 插入和删除遵循后进先出方案(LIFO)
# - 想象一副扑克牌，或者 PEZ 糖果盒
# - 主要堆栈操作:
#   - push(object):插入元素
#   - object pop():删除并返回最后插入的元素
# - 辅助堆栈操作:
#   - object top():返回最后插入的元素而不移除它
#   - integer len():返回存储的元素数量
#   - Boolean is_empty():是否不存储元素

# 堆栈的应用
# - 直接应用
#   - 网页浏览器的历史记录
#   - 文本编辑器的撤销序列
#   - 支持递归的语言中的方法调用链
# - 间接应用
#   - 算法的辅助数据结构
#   - 其他数据结构的组件


# Stack 堆栈
# Array-based Stack (using adapter pattern – array hidden by our class) 基于数组的堆栈 (使用适配器模式 - 由我们的类隐藏的数组)
# - 实现Stack ADT的一种简单方法是使用数组
# - 我们从左到右添加元素
# - 一个变量跟踪顶部元素的索引
# - 存储堆栈元素的数组可能已满
# - 然后，push操作将需要扩展数组并复制所有元素
#       S |   |   |   |   | ... |   |   |   |   |
#           0   1   2       ...       t

# Performance and Limitations
# - Performance
#   - 设 n 为堆栈中元素的数量
#   - 使用的空间为 O(n)
#   - 每个操作运行时间为 O(1)
#     (如果我们需要增加堆栈，则在 push 的情况下平摊)

# Parenthesis Matching
# 每一个 “(”, “{”, 或“[”必须搭配一个匹配 “)”, “}”, 或“]”

# 算法ParenMatch (X, n):
# 输入: 一个包含n个令牌的数组 X ，每个令牌都是一个分组符号、一个变量、一个算术运算符或一个数字
# 输出: 当且仅当 X 中的所有分组符号匹配时为 True
# 设 S 为空堆栈
# for i = 0 to n-1 do
#     if X[i] is an opening grouping symbol then
#         S.push(X[i])
#     else if X[i] is a closing grouping symbol then
#         if S.is_empty() then
#             return false {nothing to match with} 
#         if S.pop() does not match the type of X[i] then
#             return false {wrong type} 

# if S.isEmpty() then
#     return true {every symbol matched} 
# else 
#     return false {some symbols were never matched}
# 这个问题来自 2018 年的一家世界顶级媒体公司
# 我们(阿伯丁大学)的一名学生被要求完成这道问题以获得实习职位
# a parenthesis matching algorithm
from arraystack import ArrayStack
def is_matched(expr):
    '''Return True if all delimiters are properly matched'''

    lefty = "({["               # opening delimiters
    righty = "]})"              # closing delimiters
    s = ArrayStack()
    for c in expr:
        if c in lefty:
            s.push(c)           # push delimiter onto the stack
        elif c in righty:
            if s.is_empty():
                return False    # nothing to match with
            if righty.index(c) != lefty.index(s.pop):
                return False    # mismatched
    return s.is_empty()         # were all symbols matched?

# sample usage
matched = is_matched('[{{}}]')
print(matched)