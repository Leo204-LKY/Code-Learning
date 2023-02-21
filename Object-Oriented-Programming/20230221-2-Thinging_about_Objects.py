# Lecture 1.2: Thinking About Objects

# Objects 对象
# - 我们感知、感受和操纵的有形事物
#   - 人、动物、植物、汽车等

# 对象拥有：
# - Attributes 属性，如大小、形状、颜色、重量等
# - Behaviours 行为，如婴儿哭、爬、睡觉等

# Objects in Software 软件的对象
# 数据和相关行为的集合
# 建模真实项目的可重用软件组件
# Object-oriented programming 面向对象程序设计：根据交互对象的集合对复杂系统建模的编程
#
# 经典过程式(classical procedural,命令式 imperative)编程的要素:
# - 数据 - 完全被动
# - 过程：(函数 functions) - 可以操作数据

# Objects & Classes 对象和类
# 试想：我们如何分辨不同类别的对象？
# Class 类
# - 用于描述对象
# - 就像创建对象的蓝图
#   - 定义该类的所有对象共享的特定特征集。
#     - 对于给定的特征，任何特定对象都可以有不同的值。
#   - 定义该类中所有对象共享的行为。
#     - 对象上可能发生的操作。
#   - 指定与其他类的关系
#
# 例如，对于橙子，我们将其数据如下记录
#   | Orange           |
#   | ---------------- |
#   | Weight: int      |
#   | Orchard: string  |
#   | DatePicked: date |
#   | Variety: string  |
#   | Basket: basket   |
#   | ---------------- |
#   | Pick()           |
#   | Squeeze()        |
# 上面便是一个类，他可以含入(go-in)另一个类，如
#   | Basket      |
#   | ----------- |
#   | Location    |
#   | Contents    |
#   | ----------- |
#   | Transport() |
# Orange 这个类则可以包含多个对象，如
#   | orange_1234    | orange_2372 | orange_3998 |
#   | -------------- | ----------- | ----------- |
#   | 140g           | 121g        | 88g         |
#   | SunnyView Farm | Fruit Inc.  | TangyFruits |
#   | 7/8/2017       | 1/11/2017   | 3/7/2017    |
#   | Navel          | Valencia    | Mandarin    |
#   | basket_34      | basket_66   | basket_89   |
#   | -------------- | ----------- | ------------|
#   | Pick()         | Pick()      | Pick()      |
#   | Squeeze()      | Squeeze()   | Squeeze()   |

# Object-Oriented Concepts/Terminology Ⅰ 面向对象的概念/术语 1
# - 基本的构建块称为 class(类) 
# - 类实例称为 object(对象) 或 instance(实例)
# - 类的属性称为 data member(数据成员) 或 properties(属性)
# - 属性用于表示对象的状态和与其他对象的关系(state of an object & relationships to other objects)
# - 在对象上定义操作的子程序称为 method(方法) 或 member function(成员函数)
# - 对方法的调用称为 message(信息)

# Why OOP? 为什么要用 OOP？
# - Reusability 可重复使用性
#   相同的代码应该可以作为不同系统的组件使用
# - Adaptability 适应性
#   软件需要能够随着时间的推移而进化，以响应其环境中不断变化的条件。
# - Robustness 鲁棒性/坚固性
#   我们希望软件能够处理未为其应用明确定义的意外输入

# OOA vs OOD vs OOP
# 后续的课程中会详细介绍
# Object-oriented analysis(OOA) 面向对象分析
# - 查看问题、系统或任务(有人想将其转化为应用程序)并识别对象和这些对象之间的交互的过程
# - 需要做什么(需求)
# Object-oriented design(OOD) 面向对象设计
# - 将这些需求转换为实现规范的过程
# - 事情应该怎么做
# Object-oriented programming (OOP) 面向对象编程
# - 将确定的设计转化为工作程序的过程