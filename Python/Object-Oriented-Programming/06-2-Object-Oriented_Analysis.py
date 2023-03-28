# Lecture 6.2: Object-Oriented Analysis 面向对象分析

# Object-Oriented Analysis (OOA) Definition
# - “一种从类和对象的角度检查需求的分析方法。”——Grady Booch, 1995
# - 重点是寻找和描述与你的问题相关的对象
# OOA 的典型阶段
# - 查找并定义对象
# - 组织对象
# - 描述对象之间如何相互作用
# - 定义对象的外部行为
# - 定义对象的内部行为

# 步骤
# Problem Statement*1 -> Use Cases*2 -> CRC Cards -> Class Diagram (High Level)
#    -------------- Analysis Phase (Understanding the problem) --------------
# *1 <- Description of user requirements for the proposed system
# *2 <- 描述系统的使用情况
# 为了清晰，可以随时使用UML图


# CRC Card [Beck & Cunningham, 1989]
# 全称为 Class-Responsibility-Collaboration Card 类—职责—协作卡
# 目标：将域理解为对象
# - 面向对象分析是独立于语言的
# - 迫使开发人员在对象中“思考”
# 步骤(后面会详细介绍各步骤)
# - 对候选类进行头脑风暴
# - 创建初始的 CRC 卡
# - 提出该域中的使用场景
# - 使用场景(scenary)和角色扮演(role playing)来完善 CRC 卡
# 什么时候这么做？
# - 开始编程前(来有一个好的开始)
# - 添加新功能时(定期更新 CRC 卡和场景)


# 详细步骤
# 第一步 - 对候选类(class)进行头脑风暴 Brainstorming Candidate Classes
# - 写下所有与领域分析相关的对象。
#   - 关注名词(noun，对象也是名词)
#   - 好的对象会有属性(attribute)和服务(service)
# - 现在，筛选和完善候选对象:
#   - 后续处理接口(interface)
#     (不是域的一部分，这是应用程序模型 Not part of the domain, that’s the application model)
#   - 某些候选对象是否具有其他候选对象的属性？
#   - 某些类是其他类的子类吗？
#   - 是其他的一些例子吗？
#
# 候选类回顾
# 识别(Identify)
# - 名称清晰明确，被域(domain)专家认可
# - 使用单数名词作为名字
# - 以大写字母开头
# - 有责任(what 而不是 how)
# - 记忆(知识)
# - 被需要(合作)
# - 积极参与
# 分类(Filter)
# - 核心类 Core Classes
#   - 非常确定这些都在分析模型中。
# - 未决定类 Undecided Classes
#   - 可能不是类——可能是属性。
# - 取消类 Eliminated Classes
#   - 系统范围之外
#   - 应用模型类，如绑定到实现的用户界面组件

# 第二步 - CRC 卡 | CRC Cards
# - 对每一个核心候选类，各创建一个 CRC 卡
# - 什么是 CRC 卡？
#   - Class-Responsibility-Collaboration
#   - 4x6 英寸的索引(index)卡
# ---------------------------------------
# | Class Name                          |
# ---------------------------------------
# | Responsibilities | Collaborators    |
# |                  |                  |
# |                  |                  |
# ---------------------------------------
# Class Name 类名: 表示类似对象的集合 A class represents a collection of similar objects
# Responsibilities 职责/责任：类知道或做的事情
# Collaborators 协作(类)：另一个与其交互以履行其职责的类
# - E.g.:
#   - Class Name: Student
#   - Responsibilities: Name, I.D. Number, Address, Phone Number, Email; Enroll a course, Drop a course; Request transcript
#   - Collaborators: Course, Transcript

# 第三步：CRC 卡场景 Scenarios with CRC Cards
# - 创建场景
#   - 这些对象应该做什么？
#   - 如果…？
# - 处理卡片(Play the Cards)
#   - 分配角色
#   - 遍历场景
#   - 写下新的职责
#   - 添加协作类来帮助完成其职责
#   - 团队成员在参与时举起卡片(Team members hold up cards as they participate.)
# - E.g.:
#   - Bob tries to Login to the system with an incorrect password.
#   - Sally creates a new Wizard character and chooses auto-configuration.

# 一个时钟的例子
# 制作一个时钟，应该满足：可以设置当前时间；用不同格式展示时、分、秒；更新以保持与现实时间同步
# 第一次尝试…
# - Class Name: Clock
# - Responsibilities: seconds, minutes, hours, nextSecond, displayFormat, getSeconds, setSeconds, ...
# 这是一个不好的 OOAD 过程
# - 从编程的角度思考——我的数据是什么，我必须做什么？
# - 需要想一个包含协作的类群(Need to think about a community of cooperating objects!!!)
#
# 第二次尝试…
# 对时钟相关的对象进行头脑风暴 - Display, Time, Ticker/SecondTimer, Clock, Formatter
# 分类(filter) - ？
# 创建 CRC 卡 - 两种场景
# - 当计时器向时钟发出脉冲时，内部的时间表示必须增加
# - 当请求显示时，必须获取和格式化时间


# 为什么要用 CRC 卡？
# 帮助识别对象和他们的责任
# 帮助了解对象是如何交互的
# 卡片形成了设计活动的有用记录
# 卡在群体情况下工作很好,而非技术利益相关者可以理解