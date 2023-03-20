# Lecture 4.1: Queues 队列

# Queue ADT
# - Queue ADT存储任意对象
# - 插入和删除遵循先进先出(FIFO)方案
# - 插入在队列的后面，删除在队列的前面
# - 队列主要操作
#   - enqueue(object): 在队列末尾插入一个元素
#   - object dequeue(): 删除并返回队列前面的元素
# - 队列辅助操作
#   - object first(): 返回前面的元素而不删除它
#   - integer len(): 返回存储的元素数量
#   - boolean is_empty(): 表示是否没有存储元素
# - 异常 - 尝试在空队列上执行 dequeue 或 front 会抛出 EmptyQueueException

# 队列的应用
# - 直接应用
#   - 等待名单, bureaucracy
#   - 共享资源的访问(如打印机)
#   - 多道程序设计(multiprogramming)
# - 间接应用
#   - 算法的辅助数据结构
#   - 其他数据结构的组成部分

# Array-based Queue 基于数组的队列
# 以循环方式使用大小为 N 的数组
# 两个变量跟踪前面元素 r 索引的前面和后面 f 索引
# 数组位置 r 为空
# Normal configuration 
# Q  |   |   |   |   | X | X | X | X |   |   |   |
#      0   1   2       f               r
# Wrapped-around configuration
# Q  | X | X | X | X |   |   |   |   | X | X | X |
#      0   1   2       r               f

# 数组的操作
# 使用模(modul)运算符(除法余数 remainder of division)
# - 算法 size()
#   - return (N - f + r) mod N
# - 算法 isEmpty() 
#   - return (f = r)
# - 算法 enqueue(o)
#   - if size() = N - 1 then
#         throw FullQueueException
#     else
#         Q[r] <- o
#         r <- (r + 1) mod N
#   - 如果数组已满，操作enqueue将抛出异常
#   - 此异常依赖于实现(implementation-dependent)
# - 算法 dequeue()
#   - if isEmpty() then
#         throw EmptyQueueException
#     else
#         o <- Q[f]
#         f <- (f + 1) mod N
#         return o
#   - 如果队列为空，则dequeue操作将抛出异常
#   - 此异常在队列ADT中指定
# "算法"(Algorithm)是伪代码中"函数"或"方法"的另一种名称


# Queue in Python
# 使用以下三个实例变量:
# - _data: 是一个固定容量的列表实例引用
# - _size: 是一个整数，表示当前存储在队列中的元素数量(而不是数据列表的长度)。
# - _front: 是一个整数，表示队列第一个元素数据中的索引(假设队列不为空)
'''
- _data: is a reference to a list instance with a fixed capacity.
- _size: is an integer representing the current number of elements stored in the queue (as opposed to the length of the data list).
- _front: is an integer that represents the index within data of the first element of the queue (assuming the queue is not empty)
'''

class ArrayQueue:
    '''FIFO queue implemantation using a python list for underlying storage'''
    DEFAULT_CAPACITY = 10 # moderate capacity for new queues

    def __init__(self):
        '''Create an empty queue'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size
    
    def is_empty(self):
        '''Return True if the queue is empty'''
        return self._size == 0
    
    def first(self):
        '''Return (but do not remove) the element at the front of the queue
        Raise Empty exception if the queue is empty'''
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self.front]
    
    def dequeue(self):
        '''Remove and return the first element of the queue (ie FIFO)
        Raise Empty exception if the queue is empty'''
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None    # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        '''Add an element to the back of the queue'''
        if self._size == len(self._data):
            self.resize(2 * len(self._data))    # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def resize(self, cap):    # we assume cap >= len(self)
        '''Resize to a new list capacity >= len(self)'''
        old = self._data             # keep track of existing list
        self._data = [None] * cap    # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift data
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0              # front has been realigned

class Empty(Exception):
    '''Raised when the collection is empty'''
    pass # placeholder for future content

# sample usage
if __name__ == '__main__':
    myq = ArrayQueue()
    print(myq.is_empty())   # True
    myq.enqueue("hello")
    myq.enqueue(7)
    print(myq.__len__())    # 2
    print(myq.dequeue())    # hello


# 应用：Round Robin Schedulers 轮询调度程序


# Double-Ended Queues 双端队列: Deque
# 发音为'deck'，并支持在队列的前面和末尾插入/删除
# deque 是一种做"等待列表"的方法:例如，移除"第一个"人，但发现没有可用的，你可以把他们放回"开始"
# A deque is one way to do a ‘waitlist’: for example take ‘first’ person off, but discover there is nothing available, and you can put them back at the ‘start’

# 最小 deque 操作
# 我们可以将所需的函数形式化，以处理不同的场景
# - D.add_first(e):将元素 e 添加到 deque D 的前面
# - D.add_last(e):将元素 e 添加到 deque D 的后面
# - D.delete_first(): 从 deque D 中删除并返回第一个元素；如果 deque 为空，则会发生错误
# - D.delete_last(): 从 deque D 中删除并返回最后一个元素；如果 deque 为空，则会发生错误
# - D.first(): 返回(但不移除) deque D 的第一个元素；如果 deque 为空，则会发生错误
# - D.last(): 返回(但不移除) deque D 的最后一个元素；如果 deque 为空，则会发生错误
# - D.is_empty(): 如果 deque D 不包含任何元素，则返回 True
# - len(D): 返回 deque D 中的元素个数;在 Python 中，我们使用特殊方法 __len__ 来实现它
# 我们可以想象我们在deque中使用的操作(方法)的应用来证实我们的想法


# Deque 实践
# 我们可以用之前看过的ArrayQueue类来实现这一点。
# 当我们需要知道deque后面的索引时，我们可以使用模算术进行计算
# >>> back = (self._front + self._size - 1) % len(self._data)
# 另一个挑战是知道是否/何时需要再次使用模算术对 add_first 和 delete_last 方法的队列开头进行换行以减少索引
# >>> self._front = (self._front -1) % len(self._data)