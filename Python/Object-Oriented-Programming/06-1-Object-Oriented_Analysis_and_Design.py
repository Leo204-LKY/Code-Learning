# Lecture 6.1: Object-Oriented Analysis & Design 面向对象的分析与设计

# Motivation
# 编程课程会教
# - 什么是对象(Object)
# - 如何创建对象

# 缺了什么？ - 设计(Design)：找到/决定应该创建什么对象…
# - “事实上，给定应用程序和Smalltalk这样的开发系统的一组需求，‘找到对象’很容易成为有经验的OO开发人员必须面对的最困难的任务。” ——Simon Lewis, The Art and Science of Smalltalk


# Good Object-Oriented Style 好的面向对象风格
# 你可以使用任何语言,但是你如何获得可重用的、可维护的代码？
# 仅仅使用对象(object)并不能保证好的设计
# - 许多 C++ 程序只有一个类
# - 这不是好的面向对象风格！
# 任何过程都不能保证好的结果
# - 一个好的过程只会让他们更接近好的结果


# Design is a Process, Not a Waterfall
# 设计是一个迭代的活动
# - 从面向对象的分析和设计开始
# - 继续到面向对象编程
# - 必要时返回 OOA/OOD ，例如：
#   - 创建新功能时
#   - 需要用代码解决问题
# 面向对象分析只是另一种视角
# - 优秀的设计师(在任何领域)经常转换视角来创造更好的设计
# - OOA 和 OOD 的界限十分模糊
#   - OOAD方法
# 为什么称为 Waterfall(瀑布)？
# 传统的软件开发过程采用非常线性的方法——从一个阶段的输出流到下一个阶段——即为 Waterfall


# OOA 与 OOD 比较
# 理解问题所在:
# - 在分析中，我们主要关注领域模型(Domain Model)
# - 用户有什么要求？
# - 域中的对象(Object)是什么，它们如何协作？
# 理解解决方案:
# - 在设计中，我们需要集成一个应用模型(Application Model)
# - 我需要添加什么对象来让这个东西在计算机上运行，并在某种编程语言中实现？


# What is a Model and Why (You Need It)? 什么是模型？为什么需要它？
# What?
# - 模型是为了理解而对事物的抽象，无论是问题本身还是解决方案。
# - 但要记住:
#   - 最终，模型是我们对现实感知的简化…
# 建模需要一些语言/符号来表达概念
# Why?
# - 理解为什么需要一个软件系统，它应该做什么(what)，以及它应该如何做(how)
# - 传达我们对“为什么”(why)、“什么”(what)和“如何”(how)的理解
# - 发现你、我、他和她对现实的看法的共性和差异
# - 发现误解和沟通不畅