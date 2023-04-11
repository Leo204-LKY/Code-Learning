# Lecture 7.4: Data Structure: Linked List 数据结构：链表  

## 数组(array)和队列(queue)有缺点  
- 除 front 以外的任何地方的插入都是昂贵的  
- 动态数组的长度可能大于空格的个数  
- 在实时系统中，操作的平摊边界可能是不可接受的  

## 链表提供了实用的替代  
- 插入更容易，因为我们跟踪前端和(通常)尾部  
- 长度是成比例的  
- 最坏情况为 0(n)  

## Singly Linked List 串链/单向链表  
- 单链表是一种具体的数据结构，由从头指针开始的一系列节点组成  
- 每个节点存储：  
    - 元素  
    - 链接到的下一个节点  
### 列表节点的节点类  
    - 重点关注头部是否容易插入，以及节点的数量  
    - 其余的是 Node 实例  
    ```Python
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = "_element"."_next"      # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element         # reference to user's element
            self._next = next               # reference to next node
    ```

## 节点操作  
### Inserting at the Head 在链表头部插入  
![Inserting at the Head](https://user-images.githubusercontent.com/57821066/229742094-fbef5ef1-207c-4e6e-8bdd-07eff0eaf061.png)
![Algorithm](https://user-images.githubusercontent.com/57821066/229742784-31b7f896-fe88-40d8-9795-a155e399a9ba.png)
1. 分配一个新节点  
2. 插入新元素  
3. 使新节点指向原先的头节点  
4. 更新 head 指向新节点  
### Removing at the Head 删除链表头节点  
![Removing at the Head](https://user-images.githubusercontent.com/57821066/229742601-116e62c1-a365-433b-87ef-0e12102439fd.png)  
![Algorithm](https://user-images.githubusercontent.com/57821066/229742796-9280485c-fc94-4785-b13a-38d137eea08f.png)  
1. 更新head，使其指向列表中的下一个节点  
2. 允许 garbage collector 回收前第一个节点  
### Inserting at the tail 在链表尾部插入  
![Inserting at the tail](https://user-images.githubusercontent.com/57821066/229743269-b8456124-511a-4c8c-bfe2-71ac42ff11c2.png)  
![Algorithm](https://user-images.githubusercontent.com/57821066/229743281-cb05009c-0065-4c92-b652-65714306d876.png)  
1. 分配一个新节点  
2. 插入新元素  
3. 使新节点指向 `null`  
4. 旧节点指向新节点  
5. 更新尾部以指向新节点  
### 在单链表中，在尾部删除是低效的  
- 没有固定时间的方法来更新尾部以指向前一个节点  
- 我们需要在结束之前知道元素，这并不容易做到  
> - There is no constant-time way to update the tail to point to the previous node  
> - We need to know the elementbefore the end, which is not easy to do.  

## 链表实例
### Stack as a Linked List 链表堆栈  
- 我们可以用单链表实现堆栈  
- 顶部元素存储在列表的第一个节点上  
- 使用的空间为 O(n) ，堆栈 ADT 的每个操作花费 O(1) 时间  
### Queue as a Linked List 链表队列  
- 我们可以用单链表实现队列  
    - front元素存储在第一个节点上  
    - rear元素存储在最后一个节点上  
- 所使用的空间为 O(n) ，队列 ADT 的每个操作花费 O(1) 时间  
### Circularly Linked List 循环链表  
- 一个链表末尾的节点指向这个列表开头的节点  
- 应用：轮询调度器(Round Robin Schedulers)  
    - 通过重复执行以下步骤，我们可以使用队列Q实现轮询调度程序:  
        ```
        1. e = Q.dequeue()
        2. Service element e
        3. Q.enqueue (e)
        ```
### Doubly Linked List 双向链表  
- 双向链表提供了节点列表 ADT 的自然实现  
- 节点实现位置和存储:  
    - 元素(elements)  
    - 链接到的上一个节点  
    - 链接到的下一个节点  
- 特殊的 trailer 和 header 节点  
- 双向链表中的节点类  
    ```Python
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked list"""
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    ```
- 性能  
    - 包含n个元素的列表所使用的空间是O(n)  
    - 列表中每个位置所使用的空间为O(1)  
    - 所有列表的标准操作在O(1)时间内运行  
### Positional List 位置列表 - 在序列中标识一个元素  
- 为了提供元素序列的一般抽象，并具有识别元素位置的能力，我们定义了位置列表ADT。  
- 位置在更广泛的位置列表中充当标记或标记。  
- 位置p不受列表中其他位置变化的影响;一个位置变得无效的唯一方法是发出显式命令删除它。  
- 位置实例是一个简单对象，只支持以下方法:  
    - p.element():返回存储在p位置的元素。  
> 想象一下编辑器中的光标：我们只需要识别光标下面的字符。  

## 链表和数组有利有弊  
- 快速访问数组元素的索引为O(1)，因为需要先在链表中找到元素  
- 由于链表的 CPU 操作开销，等价的渐近操作（equivalent operations）在数组中更快  
- 数组使用的内存比链表少，而链表的结构决定了其内存消耗  
- 链表为操作提供了最坏的时间限制  
- 链表支持在结构的任何位置进行 O(1) 次插入和删除  