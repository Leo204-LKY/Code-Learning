# Lecture 13.1: Patterns Revisited 模式回顾  

## 模式在软件中无处不在  
以下三种模式等级/抽象程度由低到高  
- Idiom 习惯用法/风格  
    - 特定于编程语言的低级模式  
    - 描述如何使用给定语言的特性实现组件的特定方面或组件之间的关系  
- Design Pattern 设计模式  
    - 为细化软件系统的子系统/组件/它们之间的关系提供一个方案  
    - 描述了在特定上下文中解决一般设计问题的通信组件的常见循环结构  
        - 会在最后几节课中介绍
- Architectural Pattern 架构模式  
    - 表达软件系统的结构组织方案  
        - 提供一组预定义的子系统，并指定它们的职责  
        - 包括组织它们之间关系的规则和指导方针  

## *Pythonic Code* (又名 Python Idioms)  
Python 社区开发了许多约定和习惯用法：  
- 简单明了的代码是最好的  
- 每行一条语句  
- 函数单一出口原则(一个函数中最多一个 return 语句)  
- 使用 `__`（双下划线）作为一次性变量  
- 使用 `.join()` 从列表创建一个字符串  
    - 详见[这里](#string-splicing-字符串拼接)  
- ...  

一个例子：  
- ❌不要这样写：  
    ```Python
    my_container = ["Larry", "Moe", "Curly"]
    index = 0
    for element in my_container:
        print("{} {}".format(index, element))
        index += 1
    ```
- ✔️这样写：  
    ```Python
    my_container = ["Larry", "Moe", "Curly"]
    for index, element in enumerate(my_container):
        print("{} {}".format(index, element))
    ```
- 这种习惯用法称为 `Unpack 解包`  

### 更多习惯用法的例子
#### Variable Exchange 变量交换  
- ❌不要这样写：  
    ```Python
    tmp = a
    a = b
    b = tmp
    ```
- ✔️这样写：  
    ```Python
    a, b = b, a
    ```
#### List Derivation 列表推导  
- ❌不要这样写：  
    ```Python
    my_list = []
    for i in range(10):
        my_list.append(i*2)
    ```
- ✔️这样写：  
    ```Python
    my_list = [i*2 for i in range (10)]
    ```
#### One-line expression 单行表达式
- ❌不要这样写：  
    ```Python
    print("one"); print("two")

    if x == 1: print("one")

    if <complex comparison> and <other complex comparison>:
        # do something 
    ```
- ✔️这样写：  
    ```Python
    print("one")
    print("two")

    if x == 1:
        print("one")

    cond1 = <complex comparison>
    cond2 = <another complex comparison>
    if cond1 and cond 2:
        # do something
    ```
#### Indexed traversal 索引遍历  
- ❌不要这样写：  
    ```Python
    for i in range(len(my_list)):
        print(i, "-->", mylist[i])
    ```
- ✔️这样写：  
    ```Python
    for i, item in enumerate(my_list):
        print(i, "-->", item)
    ```
#### Sequence unpacking 序列解包  
- ✔️这样写：  
    ```Python
    a, *rest = [1, 2, 3]
    # a = 1, rest = [2, 3]

    a, *middle, c = [1, 2, 3, 4]
    # a = 1, middle = [2, 3], c = 4
    ```
#### String splicing 字符串拼接  
- ❌不要这样写：  
    ```Python
    letters = ["s", "p", "a", "m"]
    s = ""
    for let in letters:
        s += let
    ```
- ✔️这样写：  
    ```Python
    letters = ["s", "p", "a", "m"]
    word = "".join(letters)
    ```
#### Judgement of Truth and False 真伪判断  
- ❌不要这样写：  
    ```Python
    if attr == True:
        print("True!")

    if attr = None:
        print("attr is None!")
    ```
- ✔️这样写：  
    ```Python
    if attr:
        print("attr is truthy!")

    if not attr:
        print("attr is falsey!")

    if attr is None:
        print("attr is None!")
    ```
#### Access dictionary elements 访问字典元素  
- ❌不要这样写：  
    ```Python
    d = {"hello": "world"}
    if d.has_key("hello"):
        print(d["hello"])   # prints "world"
    else:
        print("default_value")
    ```
- ✔️这样写：  
    ```Python
    d = {"hello": "world"}

    print(d.get("hello", "default_value"))      # prints "world"
    print(d.get("thingy", "default_value"))     # prints "default_value"

    # Or
    if "hello" in d:
        print(d["hello"])
    ```
#### List of operations 操作列表  
- Example 1:
    - ❌不要这样写：  
        ```Python
        a = [3, 4, 5]
        b = []
        for i in a:
            if i > 4:
                b.append(i)
        ```
    - ✔️这样写：  
        ```Python
        a = [3, 4, 5]
        b = [i for i in a if i > 4]

        # Or
        b = filter(lambda: x: x > 4, a)
        ```
- Example 2:
    - ❌不要这样写：  
        ```Python
        a = [3, 4, 5]
        for i in range(len(a)):
            a[i] += 3
        ```
    - ✔️这样写：  
        ```Python
        a = [3, 4, 5]
        a = [i + 3 for i in a]

        #Or
        a = map(lambda i: i + 3, a)
        ```
#### File reading 文件读取  
- ❌不要这样写：  
    ```Python
    f = open("file.txt")
    a = f.read()
    print(a)
    f.close()
    ```
- ✔️这样写：  
    ```Python
    with open("file.txt") as f:
        for line in f:
            print(line)
    ```
#### Code continuation 代码续写  
- ❌不要这样写：  
    ```Python
    my_very_big_string = """For a long time I used tp go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say \"I'm going to sleep\""""

    from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
    yet_another_nice_function
    ```
- ✔️这样写：  
    ```Python
    my_very_big_string = (
        "For a long time I used to go to bed early. Sometimes, "
        "when I had put out my candle, my eyes would close so quickly "
        "that I had not even time to say \"I'm going to sleep.\""
    )

    from some.deep.module.inside.a.module import (
        a_nice_function, another_nice_function,
        yet_another_nice_function
    )
    ```
#### Explicit code 明确的代码  
- ❌不要这样写：  
    ```Python
    def make_complex(*args):
        x, y = args
        return dict(**locals())
    ```
- ✔️这样写：  
    ```Python
    def make_complex(x, y):
        return {"x": x, "y": y}
    ```
#### Use placeholders 使用占位符  
- ✔️这样写：  
    ```Python
    filename = "foobar.txt"
    basename, _, ext = filename.rpartition(".")
    ```
#### Chain comparison 链式比较
- ❌不要这样写：  
    ```Python
    if age > 18 and age < 60:
        print("young man")
    ```
- ✔️这样写：  
    ```Python
    if 18 < age < 60:
        print("young man")
    ```
#### Trinomial Operation  
- ❌不要这样写：  
    ```Python
    a = 3

    if a > 2:
        b = 2
    else:
        b = 1
    # b = 2
    ```
- ✔️这样写：  
    ```Python
    a = 3

    b = a if a > 2 else 1
    # b = 2
    ```