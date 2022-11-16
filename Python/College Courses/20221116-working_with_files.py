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