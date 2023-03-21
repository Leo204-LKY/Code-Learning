# Lecture 5.1: Files and Exception Handling

# 从文件读取信息需要做什么
# 1. 打开该文件并将该文件与一个文件变量关联起来
# 2. 读取信息的命令
# 3. 关闭文件的命令

# 打开文件
# 准备文件读取:
# A.链接文件变量和物理文件(引用文件变量就是引用物理文件)
# B.将文件指针定位在文件的开头

# 链接文件
# 格式： <file variable> = open(<file name>, "r")  # <- 这里是 r (read)
# E.g.:
# (Constant file name)
inputFile = open("data.txt", "r")
# OR (Variable file name: entered by user at runtime)
filename = input("Enter name of input file: ")
inputFile = open(filename, "r")

# 文件指针定位
# 当用'r'或'w'打开文件时，指针总是在文件顶部打开，当用'a'打开时，指针总是在文件末尾打开以追加新行
# 也可以使用 seek(k) 或 read(k) 来按 k 千字节定位游标

# 从文件读取信息
# 通常，读取是在循环体内完成的
# 每次执行循环都会将文件中的一行读入字符串
# 格式：
# for <variable to store a string> in <name of file variable>:
#     <Do something with the string read from file>
# E.g.:
for line in inputFile:
    print(line) # Echo file contents back onscreen

# 关闭文件
# 虽然当程序结束时文件会自动关闭，但在程序完成后立即显式关闭文件仍然是一个很好的习惯
#   - 如果程序遇到运行时错误并在它到达终点之前崩溃怎么办?输入文件可能会保持“锁定”状态，即无法访问的状态，因为它仍然是打开的
# 格式：<name of file variable>.close()
# E.g.:
inputFile.close()

# 将上面的操作结合，构成文件读取的基本步骤
# E.g.: 在线例子 grades1.py ，读取 letters.txt 或 gpa.txt
inputFileName = input("Enter name of input file: ")
inputFile = open(inputFileName, "r")
print("Opening file", inputFileName, " for reading.")

for line in inputFile:
    print(line) # or do whatever else is needed

inputFile.close()
print("Completed reading of file", inputFileName)


# 向文件写入信息需要做什么
# 1. 打开该文件并将该文件与一个文件变量相关联(文件在写入时被“锁定”)
# 2. 写入信息的命令
# 3. 关闭文件的命令

# 打开文件
# 格式：<name of file variable> = open(<file name>, "w")  # <- 这里是 w (write)
# E.g.:
# (Constant file name)
outputFile = open("gpa.txt", "w")
# OR (Variable file name: entered by user at runtime)
outputFileName = input("Enter the name of the output file to record the GPA's to: ")
outputFile = open(outputFileName, "w")

# 向一个文件写入
# 你可以将'write()'函数与文件变量结合使用。
#   - 请注意，此函数只接受字符串形参(其他参数必须先转换为此类型)
# 格式： outputFile.write(temp)
# E.g.:
# Assume that temp contains a string of characters.
temp = "String"
outputFile.write (temp)

# 关闭文件
outputFile.close()

# 将上面的操作结合，构成文件写入的基本步骤
# E.g.:
# Name of the online example: grades2.py
# Input file: “letters.txt” (sample output file name: gpa.txt)
inputFileName = input("Enter the name of input file to read the grades from: ")
outputFileName = input("Enter the name of the output file to record the GPA's to: ")

inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")

print("Opening file", inputFileName, " for reading.")
print("Opening file", outputFileName, " for writing.")
gpa = 0

for line in inputFile:
    if (line[0] == "A"):
        gpa = 4
    elif (line[0] == "B"):
        gpa = 3
    elif (line[0] == "C"):
        gpa = 2
    elif (line[0] == "D"):
        gpa = 1
    elif (line[0] == "F"):
        gpa = 0
    else:
        gpa = -1
temp = str (gpa)
temp = temp + '\n'
print (line[0], '\t', gpa)
outputFile.write (temp)

inputFile.close ()
outputFile.close () 
print ("Completed reading of file", inputFileName)
print ("Completed writing to file", outputFileName)


# 读取文件常用算法/步骤
# 伪代码：
# - 从文件中读取一行作为字符串
# - 当(字符串不是空的):
# -     处理行
# -     从文件中读取另一行
# 英文版：
# – Read a line from a file as a string
# – While (string is not empty):    
# –     process the line
# –     Read another line from the file


# 数据处理：文件
# 如果存在预定义的格式，则可以使用文件存储复杂的数据。
# 示例输入文件的格式:'employees.txt'
#   - <Last name><SP><First Name>,<Occupation>,<Income>
# EMPLOYEES.TXT
# Adama Lee,CAG,30000
# Morris Heather,Heroine,0
# Lee Bruce,JKD master,100000
BONUS = 0.5
inputFile = open ("employees.txt", "r")
print ("Reading from file input.txt")
for line in inputFile:
    name,job,income = line.split(',')
    last,first = name.split()
    income = int(income)
    income = income + (income * BONUS)
    print("Name: %s, %s\t\t\tJob: %s\t\tIncome $%.2f"%(first, last, job, income))
print ("Completed reading of file input.txt")
inputFile.close()


# Serialisation 序列化
# 在内存中有一个 data structure 数据结构(data objects 数据对象)，你想将它保存在一个文件中，这样您就可以重新加载并使用它
# Python Pickle模块
# - 布尔值、整数、浮点数、复数、字符串、字节对象、字节数组和 None
# - 列表、元组、字典和包含任何原生数据类型组合的集
# - 列表、元组、字典和包含任何列表、元组、字典和包含任何原生数据类型组合的集
# - 函数、类和类的实例(有注意事项)
# 例子：
# Creating a data structure
entry = {}
entry["title"] = "Dive into history, 2009 edition"
entry["article_link"] = "http://diveintomark.org/archives/2009/03/27.dive-into-history-2009-edition"
entry ["comments_link"] = None
entry["internal_id"] = b"\xDE\xD5\xB4\xF8"
entry["tags"] = ("diveintopython", "docbook", "html")
entry["published"] = True

# Save it into a file
import pickle
with open("entry.pickle", "wb") as f:
    pickle.dump(entry, f)

# 在另一个文件中：
# Load it for reuse
# >>> import pickle
with open("entry.pickle", "rb") as f:
    entry = pickle.load(f)
print(entry)
# 输出前面保存的字典及内容

# 其他保存方式
# JSON 文件
import json
with open("entry.json", "r", encoding="utf-8") as f:
    entry = json.load(f)

# CSV 文件
# 使用csv库从逗号分隔的值文件中读取数据。逐行读取文件，将每行作为数组进行操作
# 使用换行标志，以便在平台(platform)上正确地解释行结束符
import csv
with open("USGS_WC_eartag_deployments_2009-2011.csv", newline="") as f: # open the file to read it into the database
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        """ we could do something with this data, such as move it into a database, or process it by extracting items as here, being sure to convert them to the format required
        """
        bearID = int(row[0])
        pTT_ID = int(row[1])
        capture_lat = float(row[6])
        capture_long = float(row[7])
        sex = row[9]
        age_class = row[10]
        ear_applied = row[11]

    print("Finished parsing")
f.close() # close the file