# while statement
# allow us to execute a block of code repeatedly provided a certain condition is True
# also referred to as indefinite execution
# >>> while <condition>:
# >>>     body
# Example:
i = 0
while i < 10: # condition, it will check everytime before the loop
    print(i)  # body
    i += 1    # i + 1
# When i < 10 is False, the loop will exit

print("")
# break statement
# used to exit a loop and prevent the loop body from executing regardless of whether the while condition is true
# Example:
i = 0
while i < 5:
    if i == 3:
        break
    # When i == 3 is True, the while loop will exit
    i += 1
    print(i)

print("")
# continue statement
# allow us to stop the current literation (stop the while loop body from executing) and move to the next literation
# 当条件为 True 时，跳过本次循环剩余内容，进入下一次循环（而不是像 break 一样直接结束循环）
# Example:
i = 0
while i < 5:
    i += 1
    if not i % 2:
        continue
    # if i % 2 == 0 is not True, stop the current literation and move to the next one
    print(i)

print("")
# for statements with range
# range(start, stop[, step])
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0, 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0, 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0, 5） 等价于 range(0, 5, 1)
# Example1:
x = range(5)
for i in x:
# i is assigned the value of the first element in the sequence (i = 1 in this situation)
# or we can use:
# >>> for i in range(5):
    print(i)
# will print 0, 1, 2, 3, 4 in different lines
print("")
# Example2:
# Print odd numbers between 1 and 8
for i in range(1, 8, 2):
    print(i)

print("")
# for statement with else
# 如果 for 函数正常结束运行，则会继续执行 else 中的代码
# 若 for 函数由 break 结束运行，则不会执行 else 中的代码
# Example:
for i in range(1, 10):
    if i == 3:
        # break
        # 当此处的 break 不为注释时，程序会在 i == 3 为 True 时结束循环，并且不会执行 else 中的代码
        # 当此处的 break 为注释（即不满足情况或不存在 break）时，程序会在 i == 9 时结束循环，并且会执行 else 中的代码
        # 或者这么解释：当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在 else 子句则执行 else 子句，没有则继续执行后续代码；如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，则else子句不会被执行，程序将会直接跳过 else 子句继续执行后续代码
        # 来自：https://www.cnblogs.com/lybigdata/p/10037190.html
        pass
    print(i)
else:
    print("执行 else...")


print("")
# Nested fot loop
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("")

print("")
# Iterables: Strings / Lists / Tuples
# * 列表(list)和元组(tuple)会在之后学习
# a string / list is also an iterable and we can use a for loop to literate over it
course = "JC1001"
for i in course:
    print(i)
    # Output is J, C, 1, 0, 0, 1 in different lines

print("")
score = ["A", "B", "C"]
for i in score:
    print(i)
    # Output is A, B, C in different lines

print("")
colors = ("red", "green", "blue")
for i in colors:
    print(i)
    # Output is red, green, blue in different lines

print("")
# Iterables and Iterators 迭代对象与迭代器
# - Strings, lists and tuples are iterable objects
# - An iterable object can return an iterator via the i te r function
# - An iterator is an object that allows us to perform iteration
# - Using an iterator we can get to the next element using the next function
# 介绍：https://www.runoob.com/python3/python3-iterator-generator.html
course = "JC1001"
course_iter = iter(course)
while True:
    try:
        print(next(course_iter))
    except StopIteration:
        pass