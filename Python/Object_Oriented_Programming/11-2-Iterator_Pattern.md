# Lecture 11.1: *Iterator* Pattern 迭代器模式  

| Pattern | Iterator |
| --- | --- |
| 名称 | Iterator 迭代器（也称 Enumeration 枚举） |
| 递归（Recurring）问题 | 如何遍历集合中的所有对象？您不希望在集合更改时更改客户端代码。想要同样的方法。 |
| 解决方案 | 1. 每个类实现一个接口，并且<br>2. 有一个可以处理所有集合的接口 |
| 结果 | 可以更改集合类的详细信息，而无需更改遍历集合的代码 |

## GoF 版本的迭代器  
![GoF Version of Iterator](https://user-images.githubusercontent.com/57821066/234446577-4436cbdc-d7a9-485e-8125-743d42c41556.png)  
### 迭代器模式 & Python  
- 迭代器内建于 Python 中
    ```Python
    for x in [1, 2, 3]:
        # do something with x
    ```
- 这个语法隐藏了很多有趣的细节
    - 内建函数 `iter()` - 接受一个可迭代对象并返回一个迭代器  
    - 迭代器上的内建方法 `next()` 给出下一个元素  
    - 如果没有更多元素，迭代器将引发 `StopIteration` 异常  
        ```
        >>> x = iter([1, 2, 3])
        >>> x
        <listiterator object at 0x1004ca850>
        >>> next(x)
        1
        >>> next(x)
        2
        >>> next(x)
        3
        >>> next(x)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        StopIteration
        ```

## Iterables vs. Iterators  
### ***ITERABLE* 可迭代的**是  
- 任何可以循环的东西(即你可以遍历一个字符串或文件)，或  
- 任何可以出现在 for 循环右侧的内容： `for x in *iterable*: ...` ，或  
- 任何可以用 `iter()` 调用并返回 *ITERATOR* 的东西：`iter(obj)` ，或  
- 一个对象，定义了 `__iter__` 返回一个新的 *ITERATOR* 的对象，或有一个适合索引查找的 `__getitem__` 方法  
### ***ITERATOR* 迭代器**是  
- 一个具有状态的对象，可以在迭代过程中记住它的位置  
- 有一个 `__next__` 方法，可以  
    - 返回下一次迭代的值  
    - 更新状态以指向下一个值  
    - 迭代完成时抛出 `StopIteration` 异常  
- 并且它是自迭代的（self-iterable ，意味着它有一个 `__iter__` 方法返回 `self`）  

内置函数 `next()` 调用传递给它的对象的 `__next__` 方法  

## 创建和使用迭代器  
### 创建迭代器  
以创建一个 `CapitalIterable` 类为例，这个类循环遍历字符串中的每一个单词，并以首字母大写的形式输出它们  
**注意：这里使用的方法十分冗长(verbose)**  
```Python
class CapitalIterable:
    def __init__(self, string):
        self.string = string
    
    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self
```
### 使用迭代器  
```Python
iterable = CapitalIterable("the quick brown fox jumps over the lazy dog")

iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
```
实际上，Python 提供了更简单的方式：  
```Python
for i in iterable:
    print(i)
```
输出为：  
```
The
Quick
Brown
Fox
Jumps
Over
The
Lazy
Dog
```
虽然这个形式看起来不完全是面向对象的——但它背后有很多面向对象的巧妙之处！  