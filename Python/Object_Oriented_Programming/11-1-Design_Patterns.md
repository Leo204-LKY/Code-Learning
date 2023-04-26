# Lecture 11.1 Design Patterns 设计模式  

## 模式  
> 模式可以作为设计城市和建筑的辅助手段。  
> ——克里斯托弗·亚历山大（Christopher Alexander），美国建筑师  
- 模式是一个上下文中标准问题的重复解决方案。  
- “模式描述了在我们的环境中反复出现的问题，然后描述了该问题的解决方案的核心，以这样一种方式，你可以使用这个解决方案一百万次，而不必以同样的方式做两次。”  

### 工程（Engineering）中的模式  
- 其他设计师如何选择和使用模式？  
    - 成熟的工程学科有手册描述已知问题的成功解决方案  
    - 汽车设计师不会根据物理定律从头开始设计汽车  
        - 他们重用具有成功记录的标准设计，从经验中学习  

软件工程师应该使用模式吗？为什么？
- 从头开始开发软件是昂贵的
- 模式支持软件架构和设计的重用
> …我可以告诉你如何制作一件衣服，通过指定剪刀穿过一块布的路线，根据切割的角度和长度。或者，我可以给你一个模式。阅读规范时，您将不知道正在构建什么，或者当您完成时是否构建了正确的东西。模式预示着产品:它是制造产品的规则，但在许多方面，它也是产品本身。  
> ... I could tell you how to make a dress by specifying the route of a scissors through a piece of cloth in terms of angles and lengths of cut. Or, I could give you a pattern. Reading the specification, you would have no idea what was being built or if you had built the right thing when you were finished. The pattern foreshadows the product: it is the rule for making the thing, but it is also, in many respects, the thing itself.”  
> *Jim ‘Cope’ Coplein, One of the founders of the 
software pattern discipline; laid foundations of both 
Scrum and Extreme Programming.*  

## The Gang of Four (GoF) “四人帮”模式  
- 《设计模式:可重用的面向对象软件的元素》（Design Patterns: Elements of Reusable Object-Oriented Software, Addison-Wesley Publishing Company, 1994.）  
    - 由“四人帮”撰写：Dr. Erich Gamma、Dr. Richard Helm、Dr. Ralph Johnson 和 Dr. John Vlissides  
    - 书中列出了 23 种不同的模式，作为 C++ 和 Smalltalk 语言中不同类别问题的解决方案。  
    - 问题和解决方案广泛适用，被许多人使用多年  
        > 自GoF一书以来，许多其他模式也被记录下来——许多进一步的书籍、国际会议……  
        > Many other patterns have been documented since the GoF book - many further books, international conferences…  
    - https://hillside.net/patterns/  

- 该书将 23 种模式分为三类：  
    - 生成模式 Creational Patterns ：处理类和对象的初始化和配置  
        - Abstract Factory  
        - Builder  
        - Factory Method  
        - Prototype  
        - Singleton - *Factory for creating a single instance.*  
    - 结构模式 Structural Patterns ：主要处理类和对象的静态组合和结构  
        - Adapter  
        - Bridge  
        - Composite  
        - Decorator - *Extends an object transparently.*  
        - Façade  
        - Flyweight  
        - Proxy  
    - 行为模式 Behavioural Patterns ：处理类和对象社会之间的动态交互；他们如何分配责任  
        - Chain of Responsibility  
        - Command  
        - Interpreter  
        - Iterator - *Loop over elements in a collection.*  
        - Mediator  
        - Memento  
        - Observer  
        - State  
        - Strategy - *Select one of many algorithms.*  
        - Template Method  
        - Visitor  

## 设计模式的元素  
- GOF以结构化的格式呈现每个模式  
- 设计模式有 4 个基本元素：  
    ```
    Pattern Name:   Increases vocabulary of designers.
    Problem:        Intent, context, when to apply.
    Solution:       UML-like structure, abstract code.
    Consequences:   Results and tradeoffs.
    ```

## 设计模式不是什么  
- 设计模式**不是**  
    - 可以在类中编码并按原样重用的数据结构（即不是链表、堆栈）  
    - 复杂的领域特定设计（对于整个应用程序或子系统）  
- 如果它们不是熟悉的数据结构或复杂的特定于领域的子系统，那么它们是什么？  
    - “对通信对象和类的描述，这些对象和类是为解决特定环境中的一般设计问题而定制的。”  
    *“Descriptions of communicating objects and classes that are customized to solve a general design problem in a particular context.”*  