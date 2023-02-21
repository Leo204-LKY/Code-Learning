# Modules and packages
# 模块和包

# PIP - Package management in python
# PIP Install Packages 或 PIP Installs Python 的缩写
# PIP 是一个包管理器

# Part 1
# Modules 模块
# Python 支持在一个文件中定义函数或类，然后在另一个文件或交互模式中访问它们，这些文件就是模块
# 模块可以被导入(import)到另一个模块或者主模块中
# 主模块是在顶层和计算器模式下执行的脚本中可以访问的变量集合，换句话说，就是正在使用的脚本或程序作用域内的变量集合

# 理解主模块
# 在交互模式下启动 Python
# >>> __name__
# Output: '__main__'
# >>> print(__name__)
# Output: __main__
# __name__ 是 Python import 的特性
# 如果在导入的模块中尝试获取 __name__，则其为导入的模块名(如 File1)；而如果在主模块中使用，则其为 __main__
# 目前，我们所需要知道的是，当我们在脚本中或在交互模式中导入一些额外的功能/类/库等时，我们会引用模块的这个属性
# 库vs包vs模块：库通常是已发布的外部包，可以随时安装和下载

# 举例：创建一个模块
__name = "jpsModule"
def jpsFunction():
    print("Hey there :]")

def jpsFunction2(aString):
    return aString.split()

# 随后便可以在交互模式中导入模块
# (需要先将终端位置定位到当前文件夹)
# >>> import 20221130-1-modules_and_packages
# >>> 20221130-1-modules_and_packages.jpsFunction()
# Hey there :]
# >>> a = "one two three four"
# >>> 20221130-1-modules_and_packages.jpsFunction2(a)
# ['one', 'two', 'three', 'four']

# 也可以通过设置别名来使程序更易读
# >>> import 20221130-1-modules_and_packages.py as aMoudule
# >>> aMoudle.jpsFunction()
# Hey there :]

# More on modules
# 除了函数和类定义外，模块还可以包含可执行语句
# 这些语句可以用于初始化模块或设置特定的条件，具有特定值的变量或常量等，这是我们正在编写的程序所需要的
# 请记住，在交互模式下，一个模块只导入一次

# PIP
# 使用 PIP 可以安装名指定的包
# PIP 因其简单而被称赞
# 在终端中执行 pip list 可获取已经安装的包列表
# $pip list
# Package                Version
# ---------------------- -----------
# aiocache               0.11.1
# aiocqhttp              1.4.3
# aiofiles               22.1.0
# anyio                  3.6.2
# blinker                1.5
# certifi                2022.9.24
# ...

# 执行 pip 即可看到所有 pip 命令列表
# $pip
# Usage:
#   pip <command> [options]

# Commands:
#   install                     Install packages.
#   download                    Download packages.
#   uninstall                   Uninstall packages.
#   freeze                      Output installed packages in requirements format.
# ...

# 注意：课上使用的 CODIO 中包含两个版本的 Python (Python 2 及 Python 3)
# 直接执行 python 进入交互模式，Python 版本是 2，执行 python3 才会进入 Python 3
# 因此直接执行 pip ，会将包安装到默认的 Python 2
# 要将包安装到 Python 3，应该使用 pip3
# $pip3 install numpy


# 由于数据科学的发展和需要， Python 的需求也在增长
# 与其他语言相比，Python使许多用于数据科学的工具越来越容易访问

# Python 中的列表(list) vs NumPy 中的数组(array)
# Python 不包含内建的数组，而是使用列表
# 数组形如 [someValue1, someValue2, etc.]

# 数组作为一种表示和存储数据的方法，是数据科学的基础
# 数组因为存储在内存中的连续位置，因此其比列表速度快，这有利于数据科学中大量的数据处理
# 关于数组存储在内存中的连续位置，这也被称为参考的局部性——学习计算机体系结构和操作系统时会有更多关于这个的知识
# NumPy 还经过优化，可以与最新的CPU架构一起工作
# NumPy 是一个库/包/模块，部分是用 Python 编写的，其他部分是用 C 或 C++ (非解释语言)编写的。


# Part 2
# 使用 NumPy 创建数组
import numpy as np

anArray = np.array([1, 2, 3, 4])
print(type(np.array))
print(type(anArray))

for i in range(len(anArray)):
    print(anArray[i])
# Output:
# <class 'builtin_function_or_method'>
# <class 'numpy.ndarray'> 
# 1
# 2
# 3
# 4
print("")

# 使用元组亦可以创建数组
# 再次注意，元组中的元素必须是同一类别
anArray = np.array((1, 2, 3, 4))
print(type(np.array))
print(type(anArray))

for i in range(len(anArray)):
    print(anArray[i])
# 输出与上面相同
print("")

# ndim 方法
# 数组和其他数据结构一样，如列表、元组、字典等都有维度(dimension)
# ndim 方法可用于返回一个表示数组维度的整数
# 注意，这不是 Python 内建的方法，因此我们只能通数组一起使用(即需要导入 NumPy)
# ndim 和 len() 的区别
lone = [1001]
d0Arr = np.array(lone)

print("dimension is", d0Arr.ndim)
print("size is", len(d0Arr))
# Output:
# dimension is 1
# size is 1
print("")

ltwo = [1001, 2002, 3003]
d1Arr = np.array(ltwo)
print("dimension is", d1Arr.ndim)
print("size is", len(d1Arr))
# Output:
# dimension is 1
# size is 3
print("")

# 维度不是数组包含的元素数量，而是需要多少个轴(axes)来索引这个数组
# 例：
sArr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("dimension is", sArr.ndim)
# 这个数组需要两个轴来索引，因此 dimension 是 2
print(sArr[0][0])
print(sArr[1][0])
print(sArr[2][0])
# Output:
# dimension is 2
# 1
# 4
# 7
print("")

# 访问数组 - 可变语法
# 我们也可以用另一种语法来访问数组(列表和元组不支持)中的元素
print(sArr[0, 2])
print(sArr[1, 2])
print(sArr[2, 2])
# Output:
# 3
# 6
# 9
print("")

# 一维数组(1-D)称为向量
# 行和列之间没有区别
# 二维(2-D)或更高的数组称为矩阵
# 三维(3-D)或更高的数组也被称为张量

# 数组的 size 和 shape
# ndarray.ndim 返回数组的维度/轴数
# ndarray.size 返回数组的元素总数
# ndarray.shape 返回一个整数元组，显示每个维度存储的元素数量
sArr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("dimension is",sArr.ndim) 
print("total elements is",sArr.size)
print("axis 1 is", np.size(sArr,0))
print("axis 2 is", np.size(sArr,1))
print("shape is", np.shape(sArr))
# Output: 
# dimension is 2
# total elements is 9 
# axis 1 is 3
# axis 2 is 3
# shape is (3, 3)
print("")

arr = np.array([[[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]])
# 这个数组包含三个维度
# 第一个维度中包含两个数组
print("dimension is",arr.ndim)
# Output: dimension is 3
print(arr[0])
# Output:
# [[1 2 3]
#  [4 5 6]]
# 访问第一个数组
print(arr[0, 0])
# Output: [1 2 3]
# 访问第一个数组中的第一个元素
print(arr[0,0,0])
# Output: 1
print("")

# Part 3
# Basic statistics in Python
# Python 中的基础数据

# 在计算科学的各种研究主题中，如机器学习(Machine learning)、人机交互(HCI)、人工智能(AI)等，在查看一些由一组数字组成的数据时，通常有3个值值得考虑：
# Mean 平均数 - 一组数字的平均值
# Median 中位数 - 一组数字的中点
# Mode 众数 - 出现频率最高的值

# 平均数(mean)
l = [10, 20, 30, 40, 50]
# 手动计算
nOfL = len(l)
sL = sum(l)
print("mean =", sL / nOfL)
# Output: mean = 30.0
# 使用 NumPy 计算
l = np.array([10, 20, 30, 40, 50])
print("mean =", np.mean(l))
# Output: mean = 30.0
# note we don’t have to use an NumPy array
# we could have used a list
print("")

# 中位数(median)
import math
l = [10, 20, 30, 40, 50]
# 手动计算
print("median =", l[math.ceil(len(l) / 2) - 1])
# math.ceil() 会四舍五入到最近的整数，必要时返回结果
# Output: median = 30
# 使用 NumPy 计算
print("median =", np.median(l))
# Output: median = 30.0
print("")

# 众数(mode)
l = [19, 8, 29, 35, 19, 25, 15]
# 手动计算
f = {}
for i in l: # go through l
    if i in f: # if a number in l is in f
        f[i] += 1 # increment the value of l in f
    else:
        f[i] = 1 # otherwise the value of l in f is 1
m = max(f, key = f.get) # get key with highest value in f
print("mode =", m)
# Output: mode = 19
# 使用 SciPy Stats 计算
from scipy import stats
m = stats.mode(l)
print("mode = ", m)
# output is more descriptive 输出更具描述性
# Output: mode = ModeResult(mode=array([19]), count=array([2]))
# 此外在这段输出之前还会有一段 FutureWarning ，在这里不用理会
print("")

# 标准差(standard deviation)
# 标准差指的是一组或一组数字的变化或分散
# 较低的标准差表明大多数数字接近平均值，较高的标准差表明数字分散在更大的范围内
#
# 标准差的计算
# 公式在网络上可以查到
# 1. Calculate the mean
# 2. For each number: subtract the mean and square
# 3. Calculate the mean squared differences
# 4. Calculate the square root
#
# 手动计算
# import math
l = [9, 2, 5, 4, 12,
    7, 8, 11, 9, 3,
    7, 4, 12, 5, 4,
    10, 9, 6, 9, 4]
mL = sum(l) / len(l) # Step 1
mSd = []
for i in l:
    j = (i - mL) ** 2 # Step 2
    mSd.append(j)
v = sum(mSd) / len(mSd) # Step 3
print("standard deviation =", math.sqrt(v)) # Step 4
# Output: standard deviation = 2.9832867780352594
# 使用 NumPy 计算
print("standard deviation =", np.std(l)) # Step 1-4
# Output: standard deviation = 2.9832867780352594

# 百分位数(percentile)
# 百度百科：https://baike.baidu.com/item/%E7%99%BE%E5%88%86%E4%BD%8D%E6%95%B0
# 四分位将数据分成25%的组
# 第一个四分位是第25个百分位
# 第二个四分位是第50个百分位(中位数)
# 第三个四分位是第75个百分位
#
# 计算 K^(t'') 的百分位数
# 1. Order / rank all numbers in the group from small to large
# 2. Multiply K% by total number of values
#   a) If the result of 2, is not a whole number round up and go to 3
#   b) If the result is a whole number go to 4
# 3. K^(t'') percentile is the number at the index given at 2a
# 4. K^(t'') percentile is the number at the index of given at 2b
#
# 手动计算(近似值)
k = 25
l = [1, 3, 3, 4, 5, 6, 6, 7, 8, 8]
nOfL = len(l) 
#2
p = nOfL * k / 100
if not(isinstance(p,int)): 
#3
    print(k,"th percentile=",sorted(l)[int(math.ceil(p))-1])
else:
#4
    print(k,"th percentile=",sorted(l)[int(p)])
# Output: 25 th percentile= 3
# 使用 NumPy 计算
print(np.percentile(l, k))
# Output: 3.25