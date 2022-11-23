# Recursion 递归

# 简单地说，就是套娃（函数套函数）
# 使用递归可以更方便地解决部分问题

# Python 中的递归
# 函数可以自己调用自己
# 与循环一样，需要一个可以停止函数的方法，防止进入死循环

# 例如：倒计时
def countdown(n):
    print(n)
    # base case
    if n == 0:
        # finish
        return
    else:
        # recursive call
        countdown(n - 1)

countdown(5)
print("")

# 如果先调用函数再进行其他操作，称为头递归 Head recursion
def fun(n):
    if n > 0:
        fun(n - 1)
        print(n)

fun(3)
# 输出为 1 2 3
print("")

# 例：计算阶乘
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive call
    else:
        return n * factorial(n - 1)

print(factorial(4))
print("")

# 使用递归遍历列表
students = ["Emelia", ["Jim", ["Violet", "Bob"], "Kara", "Alex"], "Nia", ["Ivan", "Sarah"], "Bill"]
# 如果用 len() ，只能获得第一个列表中的元素数量
print("There are {} students.".format(len(students)))
# 输出：There are 5 students.
print("")

# enumerate 函数
# 内置的 enumerate 函数接收一个可迭代对象，并返回一个元组，其中包含一个计数(从 0 开始)和迭代可迭代对象获得的值
# 例：
seasons = ["spring", "summer", "autumn", "winter"]
print(list(enumerate(seasons)))
# 输出：[(0, 'spring'), (1, 'summer'), (2, 'autumn'), (3, 'winter')]
print("")
# 可以用 enumerate 函数获取嵌套列表的结构
for i, item in enumerate(students): 
    print(i, item)
# 输出：
# 0 Emelia
# 1 ['Jim', ['Violet', 'Bob'], 'Kara', 'Alex']
# 2 Nia
# 3 ['Ivan', 'Sarah']
# 4 Bill
print("")

# 我们需要区分列表项和嵌套列表，以获得准确的计数
# 解决方法：
# 1. 遍历列表，检查各个元素
# 2. 如果元素是列表项，即一个叶(leaf)，将它添加到一个计数(court)变量
# 3. 如果元素是列表：
#    i. 遍历嵌套列表并检查每个元素(如1所示)
#    ii. 返回到上面的列表并将发现的所有叶子添加到计数变量中

students = ["Emelia", ["Jim", ["Violet", "Bob"], "Kara", "Alex"], "Nia", ["Ivan", "Sarah"], "Bill"]

def leaf_count(aList):
    # count variable
    count = 0
    # go through the list
    for item in aList:
        if isinstance(item, list):
            # recirsive call (to go through nested list)
            count += leaf_count(item)
        else:
            count += 1
    return count

print("The number of students is {}".format(leaf_count(students)))