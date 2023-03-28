# Lecture 6.3: Object-Oriented Design & UML 面向对象设计和 UML

# 面向对象设计(OOD) - 步骤
# 面向对象分析(OOA)阶段的输出 -> 设计阶段（在软件钟解决问题）
# Analysis 分析
# - 真实情况的模型
# - What?
# System Design 系统设计
# - Overall architecture 总体架构(sub-systems s子系统)
# ---
# - 设计解决问题的高级策略。
# - 通过组织成子系统来构建系统架构(系统结构)
# - 选择控制在软件系统中的实现(控制建模)
# - 将问题划分为可实现的组件(模块化分解)
# Object Design 对象设计
# - 实现每个类的算法/数据结构
# ---
# - 系统中所有类的完整定义
# - 评估和选择实施方案
# - 设计算法来实现操作
# - 实现外部交互控制
# - 设计关联
# - 将类和关联打包成可实现的模块
# Implementation 执行
# - 将对象类和关系转换为特定的面向对象语言


# 统一建模语言(Unified Modeling Language, UML) 
# 什么是 UML? - Booch + OMT + State Charts(状态图) 的统一表示(Uniform notation)
# - 描述软件设计的图形符号
# - UML 不是一种方法或过程(不是统一发展过程[Unified Development Process]的缩写)
# 为什么要用图形化的建模语言？
# “UML是一种用于可视化、指定、构造和记录软件密集型系统工件的语言。”
# - 软件项目以团队的形式进行
# - 团队成员需要互相（有时候甚至要与最终用户）沟通
# - “一图胜千言”
#   - 问题只是用哪些词… The question is only which words...
#   - 在同一个软件工件上需要不同的视图 Need for different views on the same software artefact.

# 为什么要用 UML?
# 通过记录假设来降低风险：领域模型、需求、架构、设计、实现……
# 代表行业标准 - 更多的工具支持，更多的人理解你的图表…
# 有合理的定义(well-defined) - 虽然有解释(interpretations)和“方言”(dialects)
# 是开放的(open) - 原型(stereotype)，标签(tag)和约束(constraints)扩展基本结构(basic construct)