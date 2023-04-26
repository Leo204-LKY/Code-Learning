# Lecture 11.3: Python Comprehensions & Generators 推导式和生成器  
*不是设计模式，而是有用的 Python 功能。*  

## Comprehensions 推导式  
- 推导式是 Python 的一个非常强大的特性，允许我们在一行代码中转换或过滤一个可迭代对象  
- 考虑以下 Python 代码，它将表示整数的字符串列表转换为实际整数列表：  
    ```Python
    input_strings = ["1", "5", "28", "131", "3"]

    output_integers = []
    for num in input_strings:
        output_integers.append(int(num))
    ```
    其可以改写为  
    ```Python
    input_strings = ["1", "5", "28", "131", "3"]
    output_integers = [int(num) for num in input_strings]
    ```
    `[int(num) for num in input_strings]` 就是列表推导式  
    在 Python 中，列表推导式得到了**高度优化**，并且在循环大量项时比 `for` 循环快得多  
    - 输出为 `[1, 5, 28, 131, 3]`  
- 再看看另一个例子（使用 `if`）：  
    ```Python
    output_integers = [int(n) for n in input_strings if len(n) < 3]
    ```
    - 输出为 `[1, 5, 28, 3]`  
    推导式不仅适用于列表，还可以在 `{}` 中创建集合和字典：  
    ```Python
    from collections import namedtuple
    Book = namedtuple("Book", "author title genre")
    books = [
        Book("Pratchett", "Nightwatch", "fantasy"),
        Book("Pratchett", "Thief Of Time", "fantasy"),
        Book("Le Guin", "The Dispossessed", "scifi"),
        Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
        Book("Turner", "The Thief", "fantasy"),
        Book("Phillips", "Preston Diamond", "western"),
        Book("Phillips", "Twice Upon A Time", "scifi"),
        ]
    fantasy_authors = {b.author for b in books if b.genre == 'fantasy'}
    ```
    - 输出为 `{'Turner', 'Le Guin', 'Pratchett'}`

## Generators 生成器  
- 行为类似迭代器的 Python 函数  
- 围绕 `yield` 关键字的使用构建：  
    - 类似于 `return` 语句  
        - 退出函数并返回一个值  
        - 下次 （使用 `next()`）调用函数时，它会从它离开的地方重新开始（在 `yield` 语句之后的行）  
- Python 封装包含了 `yield` 的函数——来创建生成器对象  
- 如果我们不需要列表/集合/字典——生成器比推导式更高效  
```Python
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
```
```
>>> gen = firstn(3)
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
Traceback (most recent call last):
  File "python", line 1, in <module>
StopIteration
```
```Python
squares_list = [i**2 for i in firstn(6)] 
print(squares_list)
```
- 输出为 `[0, 1, 4, 9, 16, 25]`  