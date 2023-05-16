# Lecture 13.2: Software Architecture Patterns 软件体系架构模式  

## Architecture Patterns 架构模式  
- 简介  
    - 体系结构模式是一种**高级**抽象  
    - 它的选择是软件系统开发中的一个基本设计决策  
    - 它决定了系统范围的结构，并限制了各种子系统可用的设计选择  
    - 一般来说，它独立于要使用的实现语言  

---
- ***Layered 分层的*** - 具有层次使用关系的功能包  
- ***Data Flows 数据流*** - 被视为在进程(管道和过滤器)之间流动的数据  
- ***Client-Server 主从式架构*** [*2-tier 2层*] - 服务器组件向一个或多个客户端提供功能或服务，这些客户端发起对此类服务的请求  
- **Peer-to-Peer 点对点的/对等的** - 在具有相同状态的组件(对等体)之间划分的应用程序任务  
- **Broker 协调者** - 负责协调多个分布式对象之间通信的组件  
- **Virtual Machines 虚拟机** - 将应用程序视为用特殊用途语言编写的程序  
- ***Model-View-Controller 模型-视图控制器*** - 持用户界面的开发（对数据的多个视图）  
- **Repository 仓库/数据库** - 围绕数据构建的应用程序  

还有其他模式这里没有介绍  

## Layered Architecture 分层体系架构  
- 经典的分层架构例子——通信系统：  
    ![Communitation Systems](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/a01b7ea3-f037-4a28-bed8-507f5d2f06d6)  
- Variants 变体  
    - **Closed Layered Architecture 封闭式分层架构** - 每个层只与它下面的层交互  
    - **Open Layered Architecture 开放式分层架构** - 层可以自由地与任何其他层交互  

## Data Flow Architecture 数据流架构  
- 功能组件处理它们的输入以产生输出  
    - 通常称为 *pipe* 管道和 *filter model* 过滤器模型(如在UNIX shell中)  
    - Filter = process 进程； Pipe = input stream 输入流  
    - 过滤器可以丰富、细化或转换其输入数据  
- 这种方法的变体很常见  
    - 当转换是顺序的，这被称为 *batch sequential model* 批顺序模型，在数据处理系统中广泛使用  

    ![Classic UNIX processes & pipes…](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/9d2b1f83-0970-4536-8a30-0366bf6d62c1)  

## Client-Server Architecture 主从式架构  
- 客户端和服务器组件(程序)是分开的  
    - 通常，客户机和服务器通过在不同硬件上的网络进行通信，但客户机和服务器可能位于同一系统中  

    ![Client-Server Architecture](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/fa5c1069-2a2a-4938-8293-7a4279d69fb9)  
- **Client 客户端** - 从服务器请求内容或功能(如微软 Outlook)  
- **Server 服务端** - 为一个或多个客户端(如微软 Exchange 邮件服务器)提供功能或服务  
- 变体：  
    - **Fat Client 胖型客户机** - 客户端包含 application behaviour 应用程序行为<u>和</u> presentation behaviour 表示行为  
    - **Thin Client 瘦型客户机** - 客户端只包含表示行为  

## Model-View Controller 模型-视图控制器(MVC)
- 最初为 OOP 语言 Smalltalk 设计  
- 现在非常流行于 Web 应用程序和移动、桌面和其他客户端  
- MVC 是关于 *separation of concerns 关注点分离*的  
    - 将在用户界面中显示数据的应用程序表示层与实际处理数据的方式隔离开来  
    - 允许独立开发、测试和维护  

    ![Model-View Controller](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/18ec1d60-9933-4588-88fa-bfcc8c9967a6)  
- **Model 模型**  
    - 数据的模型或表示  
    - 提供数据的接口  
- **View 视图**  
    - 数据的表示  
    - 可以独立开发，但不应该包含任何复杂的逻辑  
        - 逻辑应该驻留在控制器或模型中  
- **Controller 控制器**
    - 接受输入并将其转换为模型或视图的命令  

    ![MVC Instance](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/867f7219-e696-4992-8088-9d79ffcb3273)
### 模型-视图控制器 & Python  
一个很简单的例子：  
```Python
class Model:
    def logic(self):
        data = "Got it!"
        print("Model: Crunching data as per business logic")
        return data

class View:
    def update(self, data):
        print("View: Updating the view with results: ", data)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print("Controller: Relaying the Client request")
        data = self.model.logic()
        self.view.update(data)
```
```Python
class Client:
    print("Client: Asking for certain information")
    controller = Controller()
    controller.interface()
```
```
Client: Asking for certain information
Controller: Relaying the Client request
Model: Crunching data as per business logic
View: Updating the view with results: Got it!
```

## Closing Summary 结语  
- 体系结构模式允许将系统分解成可以独立开发(在某种程度上)和维护的块  
- 这些模式支持大规模、长期的开发和维护  
- 不是配方（recipe），只是一种方法  
- 大型系统很少遵循单一的体系结构模式  