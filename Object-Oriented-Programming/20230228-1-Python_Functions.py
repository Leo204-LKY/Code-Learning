# Lecture 2.1 Python Functions (aka Method)  函数

# Python函数是你的朋友
# 函数(也称为 Methods 方法)让我们将思想封装在代码中，以便在需要时可以重复使用。
# 函数让我们无需重复代码就可以重复操作。
# 功能丰富，维护方便。

# 函数使用关键字 def 来定义
def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n
# 这将建立一个新的标识符(identifier)作为函数的名称(在本例中为 count )，并建立它所期望的参数数量，这定义了函数的签名(signature)
# return 语句返回该函数的值并终止其处理


# 为函数重构程序
# eg. GPA Calculator
print("Welcome to the GPA Calculator")
print("Please enter all your letter grades, one per line")
print("Enter a blank line to designate the end")
# Map from letter grade to poit value
points = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33, "D": 1.0, "F": 0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == "":
        done = True
    elif grade not in points:
        print("Unknown grade \"{0}\" being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0: # avoid division by zero
    print("Your GPA is {0:.3}".format(total_points / num_courses))

# 每次只进行一次移动，从最简单的欢迎指示开始
# 第一步：欢迎部分
def welcome():
    print("Welcome to the GPA Calculator")
    print("Please enter all your letter grades, one per line")
    print("Enter a blank line to designate the end")

# 第二步：计算部分
def calculate():
    points = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33, "D": 1.0, "F": 0.0}
    num_courses = 0
    total_points = 0
    done = False
    while not done:
        grade = input()
        if grade == "":
            done = True
        elif grade not in points:
            print("Unknown grade \"{0}\" being ignored".format(grade))
        else:
            num_courses += 1
            total_points += points[grade]
    if num_courses > 0: # avoid division by zero
        print("Your GPA is {0:.3}".format(total_points / num_courses))
    
# 第三步：添加菜单
        menu()  # 上面的 calculate 函数结束运行后，会调用菜单函数
def menu():
    print("Enter 1 to exit or 2 to convert more grades")
    choice = input()
    if choice == 1:
        exit()
    else:
        calculate()
# 有了菜单，我们可以为多名学生计算成绩

# 实际运行程序时，按顺序调用上面的函数
welcome()
calculate()


# 重复的代码应该放入函数中
# 函数应该简短
# 函数应该只做一件事
# 以小步骤进行重构，以便更容易地修复错误
# 函数应该返回一种类型，在本例中是' void '，以后我们会看到更多的类型
# 返回值的函数更容易测试