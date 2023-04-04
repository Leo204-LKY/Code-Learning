# Lecture 7.2: Testing Mehods 测试方法  

## Test Driven Development(TDD) 测试驱动开发  
“Write tests first!”  
TDD将 _“未经测试的代码是坏代码”(untested code is broken code)_ 的概念更进一步，并建议只有未编写的代码才应该未经测试  
- 在为这段代码编写完测试之前，不要编写任何代码。  
- 需求 _(requirements，或用例 use cases)_ 被转换成非常具体的测试用例(test cases)，然后对软件进行改进以通过新的测试。  
> _Refactoring 重构 - 在不改变外部行为的情况下修改代码：注释、格式、其他内部更改。_  

## Coverage Criteria 覆盖标准  
- 即使是小程序也有太多的输入，无法完全测试它们  
    - ```Python
        def computeAverage(a, b, c):
            return float(a + b + c) / 3
        ```
    - 测试人员搜索一个巨大的输入空间，试图用最少的输入来找出最多的问题  
- 覆盖标准给出了结构化的、实用的搜索输入空间的方法  
    - 彻底搜索输入空间  
    - 测试没有太多重叠  
    > - Function Coverage 功能覆盖 - 程序中的每个函数(或方法)都被调用了吗?  
    > - Statement Coverage 语句覆盖 - 程序中的每条语句都被执行了吗?  
    > - Branch Coverage 分支覆盖 - 是否执行了每个控制结构的每个分支(例如，给定一个if语句，是否执行了true分支和false分支)?  
    > - Condition Coverage 条件覆盖 - 每个布尔子表达式的值都是true和false吗?  

## Testing Activities 测试活动
1. Test Design 测试设计  
    - Criteria-based  
        - 设计测试值以满足覆盖率标准  
    - Human-based  
        - 基于程序的领域知识和测试的人类知识来设计测试值  
2. Test Automation 测试自动化  
    - 将测试值嵌入可执行脚本
3. Test Execution 测试执行  
    - 在软件上运行测试并记录结果  
4. Test Evaluation 测试评估  
    - 评估测试结果，向开发人员报告  
> Agile Methods 敏捷方法  
> - 重新定义正确性，使其相对于特定的测试集  
> - 如果软件在测试中表现正确，那么它就是“正确的”  
> - 我们不是定义所有的行为，而是演示一些行为  

## Test Automation 测试自动化
使用软件来:  
- 控制测试的执行  
- 比较实际结果和预测结果  
- 设置测试前提条件和其他测试控制  
- 管理测试报告功能  
- 降低成本  
- 减少人为错误  
- 减少来自不同个体的测试质量差异  