# Lecture 5.2: Exception Handling

# Error Handling With Exceptions 使用 Exception 处理错误
# 异常用于处理异常错误 extraordinarily errors("extraordinarily ones")。
# 通常这些是致命的运行时错误("崩溃"程序 "crashes" program)
# 示例:试图打开一个不存在的文件
# 处理异常的基本结构：
# try:
#     Attempt something where exception error may happen
# except <exception type>:
#     React to the error
# else: # Not always needed
#     What to do if no error is encountered
# finally: # Not always needed
#     Actions that must always be performed (possibly clean up work) 


# Raising your own Exceptions 引发自己的异常
# 正如我们在堆栈和队列中看到的，你也可以编写自己的异常
# 导入需要的异常模块
""" A file for exceptions"""
class Empty(Exception):
    """Raised when the collection is empty"""

# 另一个文件中：
# >>> from exceptions import empty
# 假设遇到错误：
# >>> raise Empty("Queue is empty")
# 前面学习的类(class)中有用到

# Python 中常见的异常
# Class             | Description
# Exception         | A base class for most error types
# AttributeError    | Raised by syntax obj.foo, if obj has no member named foo
# EOFError          | Raised if"end of file" reached for console or file input
# IOError           | Raised upon failure of I/O operation (e.g., opening file)
# IndexError        | Raised if index to sequence is out of bounds
# KeyError          | Raised if nonexistent key requested for set or dictionary
# KeyboardInterrupt | Raised if user types ctrl-C while program is executing
# NameError         | Raised if nonexistent identifier used
# StopIteration     | Raised by next(iterator ) if no element; see Section 1.8
# TypeError         | Raised when wrong type of parameter is sent to a function
# ValueError        | Raised when parameter has invalid value (e.g., sqrt(—5)
# ZeroDivisionError | Raised when any division operator used with 0 as divisor
#
# 中文版：
# 类                | 描述
# Exception         | 大多数错误类型的基类
# AttributeError    | 由语法 obj.foo 引发，如果 obj 没有名为 Foo 的成员
# EOFError          | 如果“文件结束”到达控制台或文件输入将引发
# IOError           | 当I/O操作失败时引发(例如，打开文件)
# IndexError        | 如果序列索引越界将引发
# KeyError          | 如果 set 或 dictionary 中不存在请求的 key 将被触发
# KeyboardInterrupt | 如果用户在程序执行时输入 Ctrl+C 将引发
# NameError         | 如果不存在标识符将被触发
# StopIteration     | 如果没有元素，则由 next(迭代器) 引发;参见章节1.8
# TypeError         | 发送给函数的参数类型错误时引发
# ValueError        | 当参数值无效时引发(例如， sqrt(-5))
# ZeroDivisionError | 当任何除法运算符使用 0 作为除数时引发

# 异常处理：文件例
# Name of the online example: file_exception.py
# Input file name: Most of the previous input files can be used e.g. "input1.txt"
import sys
inputFileOK = False
while (inputFileOK == False):
    try:
        inputFileName = input("Enter name of input file: ")
        inputFile = open(inputFileName, "r")
    except IOError:
        print("File", inputFileName, "could not be opened")
    else:
        print("Opening file", inputFileName, " for reading.")
        inputFileOK = True
        for line in inputFile:
            sys.stdout.write(line)
        print ("Completed reading of file", inputFileName)
        inputFile.close()
        print ("Closed file", inputFileName)
    finally:
        if (inputFileOK == True):
            print ("Successfully read information from file", inputFileName)
        else:
            print ("Unsuccessfully attempted to read information from file", inputFileName)


# 异常处理：键盘输入
# Name of the online example: exception_validation.py
inputOK = False
while (inputOK == False):
    try:
        num = input("Enter a number: ")
        num = float(num)
    except ValueError: # Can't convert to a number
        print("Non-numeric type entered '%s'" %num) 
    else: # All characters are part of a number
        inputOK = True
num = num * 2
print(num)