# Working with files 文件处理

# open() 函数可用于返回一个文件对象
# 通常接受两个参数
#   - 要打开文件的名称
#   - 模式
#     + r - read，默认模式 - 读取文件，若文件不存在则程序会报错
#     + a - append - 打开要添加内容的文件，若文件不存在则会创建文件
#     + w - write - 打开要修改(覆盖)内容的文件，若文件不存在则会创建文件
#     + x - create - 创建指定文件，若文件已存在则会报错
#   - 可选参数
#     + t - text，默认模式 - 文本模式
#     + b - binary - 二进制模式（如图像）

# 注意：运行前要将终端目录定位到当前目录(College Courses)，否则会报错
f = open("20221116-demofile.txt")
print(type(f))
# <class '_io.TextIOWrapper'>


# 读取文件
# 读取模式会返回文件的全部内容
f = open("20221116-demofile.txt", "r")
print(f.read())
# 通过添加参数可以指定返回的字符数
f = open("20221116-demofile.txt", "r")
print(f.read(5))
print("---")

# 使用 readline() 来返回其中一行的内容
f = open("20221116-demofile.txt", "r")
print(f.readline())
print("---")
# 可以多次调用 readline 来返回更多行
f = open("20221116-demofile.txt", "r")
for l in f:
    print(l)
# 输出时会发现每行之间还有一个空行
# readline() 从文件中读取一行;换行符(\n)留在字符串的末尾。只有文件的最后一行没有换行符。
print("---")
# 将 print() 稍作修改即可
f = open("20221116-demofile.txt", "r")
for l in f:
    print(l, end = "")
print("\n---")

# 也可以使用 list(f) 来在列表中读取文件的所有行
f = open("20221116-demofile.txt", "r")
l = list(f)
for line in l:
    print(line, end = "")
print("\n---")
# 或者使用 readlines()
f = open("20221116-demofile.txt", "r")
print(f.readlines())
# Output: ['Hello from some file.\n', 'This is on the 2nd line. \n', 'Third line.\n', 'And so on... :)']
print("")


# 关闭文件
# 使用完文件后关闭它是一个好习惯
f = open("20221116-demofile.txt", "r")
l = list(f)
for line in l:
    print(line, end = "")
f.close()
print("\n", f.closed)
print("")

# 或者，如果使用 with 关键字，我们可以对文件进行打开、创建、修改等需要的操作，文件将自动关闭
# 这种方法较为推荐
with open("20221116-demofile.txt", "r") as f:
    for line in f:
        print(line, end = "")
# 使用 f.closed 来确认文件是否已经关闭
print("\n", f.closed)
# Output: True
print("")

# 另一种方法是使用try/finally，它将确保在打开文件后，如果文件操作引发异常，文件将被正确关闭
f = open("20221116-demofile.txt", "r")
try:
    l = list(f)
    for line in l:
        print(line, end = "")
finally:
    f.close()
print("\n", f.closed)
# Output: True
print("")

# 文件对象的当前位置
# tell() 会返回一个整数，代表文件的当前位置（注意，在二进制模式下这是一个字节数，在文本模式下这是一个“不透明”数字）
# seek() 可以用于改变文件对象的位置
#   - 接受两个参数：偏移量(offset)和“从哪里”(whence)
#   - offset: 偏移量是对要移动的字节数的引用
#   - whence: 0 表示文件的开始，1 表示当前位置，2 表示文件的结束
f = open("20221116-demofile.txt", "r")
print(f.read(5))   # Move the 5th position
print(f.tell())    # Current position
f.seek(0, 0)       # Go to the start of the file
print("")

# 修改文件
# 要写入文件，我们需要创建一个file对象并向open方法添加一个参数
# a - 在文件末尾添加内容
with open("20221116-demofile-2.txt", "a") as f:
    f.write("Here's some text")
with open("20221116-demofile-2.txt", "r") as f:
    print(f.read())
# w - 覆盖已有内容
with open("20221116-demofile-3.txt", "w") as f:
    f.write("Now I have overwritten the whole file")
with open("20221116-demofile-3.txt", "r") as f:
    print(f.read())


# 创建文件
# 使用参数 x 来创建文件
with open("20221116-demofile-4.txt", "x") as f:
    f.write("Some text going in the new file.")
with open("20221116-demofile-4.txt", "r") as f:
    print(f.read())
# 如果文件已经存在，则程序会报错
# FileExistsError: [Errno 17] File exists: '20221116-demofile-4.txt'
# 使用参数 w 时，若文件不存在，也会创建文件

with open("20221116-demofile-5.txt", "x") as f:
    f.write("")

# 混合模式
# 使用混合模式可以简化代码
# r+ - 读 + 写
with open("20221116-demofile-5.txt", "r+") as f:
    f.write("Read and writting :O")
    print(f.read())
    # 输出为空
    # 原因：在调用write方法后，文件对象的当前位置移动到文件的末尾。我们可以使用 tell() 方法来验证这一点
    print(f.tell())
    # 因此需要使用 seek(0) 来将位置移动到文件开头
    f.seek(0)
    print(f.readline())
    # 注意：每次，文件的内容都被手动删除
print()

# w+ - 写 + 读
with open("20221116-demofile-6.txt", "w+") as f:
    f.write("Writting then read :O\n")
    f.seek(0)
    print(f.readline())

# a+ - 写 + 读
# 会在文件后添加内容
with open("20221116-demofile-7.txt","a+") as f: 
    print(f.tell())
    f.seek(0) 
    print(f.readlines()) 
    f.write("append this :)\n") 
    f.seek(0)
    print(f.readlines())

print("")


# OS Module 操作系统服务模块
# 提供各种函数，允许我们的程序与文件系统和运行 Python 的底层系统的其他方面进行交互
# 在文件头使用 import os 来使用此模块
import os
# 如果使用的是交互模式（如在终端中执行 Python 命令后的界面），我们必须先执行 import os，才能使用模块提供的任何方法
# >>> import os
# 其中一些命令类似于它们的 bash 对应命令

# 查看当前目录的 Bash 命令是 pwd
# 如：Linux 终端中使用 $pwd
# 交互模式下
# >>> os.getcwd()
# 返回当前所在目录
current_dir = os.getcwd()
print(current_dir)

# 创建文件夹的 Bash 命令是 mkdir
os.mkdir("aFolder")

# 修改目录的 Bash 命令是 cd
os.chdir("aFolder")
os.getcwd()