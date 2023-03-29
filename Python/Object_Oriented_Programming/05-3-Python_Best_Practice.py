# Lecture 5.3: Pyhton Best Practice
# Marked as Lecture 5.1 & Lecture 5.2 in lecture slides

# The Zen of Python | Python 之禅
# PEP 20 - 在交互模式中输入"import this"
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!


# Python Enhancement Proposals (Python 增强建议，PEP)
# Python对它应该如何使用很固执己见 Python is opinionated about how it should be used.
# 使用 PEP 文档索引来了解更多信息: https://www.python.org/dev/peps/
# 几个关键的标准:
# PEP 8 - Python代码风格指南： https://www.python.org/dev/peps/pep-0008/
# PEP 257 - 文档字符串约定： https://www.python.org/dev/peps/pep-0257/
# 如果需要，也可以讨论其他专业话题 Maybe others on specialist topics as required

# Python anti-patterns | Python 反模式 - Worst practices 最差实践
# Correctness 正确性：反模式会破坏您的代码或使其做错误的事情
# Maintainability 可维护性：使代码难以维护或扩展的反模式
# Readability 可读性：使代码难以阅读或理解的反模式
# Performance 性能：会不必要地降低代码速度的反模式
# Security 安全性：对程序构成安全风险的反模式
# Migration 迁移：帮助您更快地迁移到框架新版本的模式

# Correctness 正确性
# 以下内容的实例可以在这里找到：https://docs.quantifiedcode.com/python-anti-patterns/correctness/index.html
# Bad Practices:
# - 从类外部访问受保护的成员
# - 赋值给内置函数（如给 list 赋值 [1, 2, 3]）
# - 不良 except 顺序
# - else 子句在循环(如 while)中没有 break 语句
# - 执行 Java 风格的 getter 和 setter
# - 使用制表符(tab) （根据 PEP 8 风格指南，所有 Python 代码应该一致地缩进4个空格）
# - 没有在循环中适当的地方使用 else
# - 不使用显式解包
# - 不使用 get() 从字典中返回默认值
# - 不使用 setdefault() 初始化字典

# Maintainability 可维护性
# 如果一个程序很容易理解和修改代码，即使对不熟悉代码库的人来说也是可维护的
# 以下内容的实例可以在这里找到：https://docs.quantifiedcode.com/python-anti-patterns/maintainability/index.html
# Bad Practices:
# - 使用通配符导入: from math import *
# - 不使用 with 打开文件
# - 从函数调用返回多个变量类型 - 调用方在继续处理前需要先判断返回值的类型
# - 使用 global 语句来让函数访问或修改全局变量
# - 使用单个字母（如 a, b, c）来命名变量

# Readability 可读性
# 以下内容的实例可以在这里找到：https://docs.quantifiedcode.com/python-anti-patterns/readability/index.html
# Bad Practices:
# - Asking for permission instead of forgiveness 请求允许而不是请求原谅（EAFP - 请求原谅比请求允许更容易["先做再说，有错就抛异常"]，意思是应在使用 try-except 而不是 if）
# - 使用错误的方式将变量与 None 比较（应使用 <variable> is None 而不是 <variable> == None，后者也可以，但不符合 PEP 8 标准）
# - 不使用字典推导式（应直接使用 {} 创建字典而不是 dict()）
# - 从函数返回多个值时不使用命名元组
# - 使用非 Python 循环
# - 在函数名中使用驼峰式大小写

# Security 安全性
# 使用 exec：https://docs.quantifiedcode.com/python-anti-patterns/security/use_of_exec.html

# Performance 性能
# 使用 key in list 检查 key 是否包含在 list 中：https://docs.quantifiedcode.com/python-anti-patterns/performance/using_key_in_list_to_check_if_key_is_contained_in_a_list.html


# 关于 Anti-Patterns 的更多信息：https://docs.quantifiedcode.com/python-anti-patterns/index.html

# Further Reading:
# Python的最佳实践(BOBP)指南
# 在语言、风格、测试等方面有很多有用的建议
# https://gist.github.com/sloria/7001839