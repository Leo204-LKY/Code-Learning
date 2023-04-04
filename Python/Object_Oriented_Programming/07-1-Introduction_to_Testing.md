# Lecture 7.1: Introduction to Testing  

## Software Testing  
### 为什么要测试  
- 提高质量  
- 降低成本  
- 保证用户满意度  
### 测试  
- 通过观察软件的执行情况来评估软件。  
- 测试是软件开发中最耗时、最昂贵的部分  
  - 不测试成本更高！  
- 测试人员的目标是尽可能早地消除故障  

- 运行程序和修复错误是一种粗略的测试方式。  
- 改变几行代码可以影响开发人员没有实现的程序的部分内容,这将受到更改的影响,因此不会测试它  
- 随着程序的发展,解释器可以通过该代码的各种路径也会增长,而且很快就无法手动测试它们。  


## Faults, Failures & Errors  
这三个概念与 Bug 不同  
### Software Fault  
可译为“故障”  
- 软件中的静态缺陷  
- 可能导致系统或功能失效的异常条件  

### Software Failure  
可译为“失效”  
- 关于需求或预期行为的其他描述的外部的不正确行为  
- 当一个系统不能执行所要求的功能时  

### Software Error  
可译为“错误”  
- 错误的内部状态，是某些错误的表现  
- 计算、观察或测量值或条件，与真实、规定或理论上正确的值或条件之间的差异。Error是能够导致系统出现Failure的系统内部状态  


## Testing Goals 测试目标  
- Level 0：测试(testing)和调试(debugging)之间没有区别   
  - 不能帮助开发可靠或安全的软件  
- Level 1：测试的目的是显示正确性  
  - 正确(correctness)是不可能实现的  
- Level 2：测试的目的是证明软件不能正常工作  
  - 寻找失败(failure)是一种消极的行为  
- Level 3：测试的目的不是证明任何具体的东西，而是降低使用软件的风险  
  - 测试人员和开发人员必须合作以降低风险  
- Level 4：测试是一门帮助所有IT专业人员开发更高质量软件的学科  


## Traditional vs OO Testing 传统测试 vs 面向对象测试  
### 传统测试 Levels  
- Acceptance Testing 验收测试：软件是否为用户所接受?  
- System Testing 系统测试：测试系统的整体功能  
Integration Testing 集成测试：测试模块之间的交互方式  
- Module Testing (Developer Testing) 模块测试(开发者测试)：测试每个类、文件、模块、组件  
- Unit Testing (Developer Testing) 单元测试(开发者测试)：每个单元(方法)单独测试  

### OO 测试 Levels  
- Inter-Class Testing 交互类测试：一起测试多个类  
- Intra-Class Testing 内部类测试：以调用序列的形式测试整个类  
- Inter-Method Testing 交互方法测试：测试同一类中的方法对  
- Intra-Method Testing 内部方法测试：分别测试每个方法