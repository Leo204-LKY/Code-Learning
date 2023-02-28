# Lecture 1.3 & 1.4: OOP Principles Ⅰ & Ⅱ OOP 原则 1 & 2

# OOP 的关键原则
# 面向对象编程语言的特点:
# - Encapsulation & Information-Hiding 封装和信息隐藏
# - Abstraction 抽象
# - Inheritance 继承
# - Association, Composition & Aggregation 关联、组合和聚合
# - Polymorphism 多态

# Encapsulation 封装
# - 其必须能够定义一个包含数据和访问(操作)数据的子程序的单元
#
# Information-Hiding 信息隐藏
# - 从与对象交互的对象中隐藏对象的实现细节
# - 将外部视图(behaviour 行为)与内部视图(state 状态)分开
#   - Public Interface 公共接口
#     - 对象提供的属性和操作的集合
#
# Abstraction 抽象
# 抽象意味着处理最适合给定任务的细节级别
# - 抽象是一个实体的视图或表示，它只包括其最基本的属性(其最重要的属性)
# - 抽象的概念是编程(和计算机科学)的基础
# - 我们处理复杂性的基本方式之一
#   - 几乎所有的编程语言都支持用子程序进行过程抽象
#   - 自 1980 年以来设计的几乎所有编程语言都支持数据抽象
#
# Inheritance 继承
# - 在许多面向对象语言中，术语继承被用来描述包容(subsumption，即is-a)关系
#   - 例：An orange *is-a* fruit 橙子是一种水果
#   - 包容提供了创建子类(subclass)的能力
#   - 子类共享父类的结构和/或行为
# - 从一个类(单继承)或多个类(多继承)继承
# - 继承的一个缺点:
#   - 创建类之间的相互依赖关系，使代码维护复杂化
# - Method Overriding 方法覆盖/方法重写
#   - 除了继承方法，类还可以修改继承的方法
#   - 新的覆盖继承的 - 即方法覆盖
# - Multiple Inheritance 多重继承
#   - 强大的机制，允许子类继承多个父类
#   - 不是所有的面向对象语言语言都支持它
#   - 如果我们继承了两个提供重叠接口的类，可能会很混乱
# - Abstract Classes & Methods抽象类和方法
#   - 有时候在超类中提供一个方法的默认实现是没有意义的。
#   - 相反，我们希望指定该方法在任何子类中都是必需的。
#   - 通过创建一个或几个带有适当方法的抽象类来实现。
# - 抽象方法基本上是这样的:
#   - "We demand this method exist in any non-abstract subclass, but we are declining to specify an implementation in this class."
#   - 我们要求这个方法存在于任何非抽象子类中，但我们拒绝在这个类中指定实现
#
# Association, Composition & Aggregation 关联、组合和聚合
# - 对于那些显而易见的 is-a 包容关系来说，继承是完美的解决方案，但它也可能被滥用
# - 面向对象语言的程序员时常忘记类与对象之间还有其他联系
# - Association 联系
#   - 最简单的关系。
#     - 一个类使用另一个类提供的功能
#     - 如前面的 Orange-Basket 例子
# - 一些特殊的联系(association)
#   - Composition (part-of, 成分/构成) - 子类离开父类就不能存在
#   - Aggregation (has-a, 剧集/聚合) - 子类可以独立于父类存在
#
# Polymorphism 多态
# - 源自希腊语，意思是许多(多边形)形状(变形)。
# - 存在几种不同类型的多态，不同的面向对象语言或多或少地支持多态
# - Method Overloading 方法重载
#   - 一个类，有两个或多个方法，具有相同的名称，但不同的参数列表和不同的行为。
# - Subtyping 子类型化
# 允许一个方法被写入一个特定类 B 的对象，但也可以正确工作，如果传递一个属于类 S 的对象，是 B 的一个子类。(Allows a method to be written to take an object of a certain class B, but also work correctly if passed an object that belongs to a class S that is a subclass of B.)

# Object-Oriented Concepts/Terminology Ⅱ & Ⅲ 面向对象的概念/术语 2 & 3
# - 对象提供给其他人与之交互的属性和操作是它的public interface(公共接口)
# - 继承的类是 derived class(派生类) 或 subclass(子类)
# - 另一个类继承的类是 base class(基类) 或 superclass(超类)
# - 当子类提供继承方法的自己版本时，这是 method overriding(方法重写)
# - 当一个类有两个或多个同名的方法，但参数列表和行为不同时，这是 method overloading(方法重载)
# - 声明方法但不实现方法的类是 abstract class(抽象类)