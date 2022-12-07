# Sorting and searching
# 排序和搜索

# 时间/空间复杂性介绍
# 正如你可能猜到的那样，编程涉及到数据结构和算法
# 有些算法比其他算法更有效
# 为了确定哪个算法比另一个算法更有效，我们使用复杂性分析

# 时间复杂性 Time complexity
# 用输入量来描述算法完成所需时间的函数
# 独立于实际时间，即手表上的时间
# 这是因为其他因素可能会影响实际时间，例如哪种类型的语言/硬件/编译器或虚拟机优化等。

# 空间复杂性 Space complexity
# 一个函数，根据输入的数量/大小来描述算法所需的内存量
# 有时我们需要考虑额外的内存来存储输入本身
# 不使用特定的内存单位(例如字节)，我们再次尝试保持独立于这些度量，只使用简单的数字来表示空间复杂性
# 有时我们不使用空间复杂度，特别是当所使用的空间非常小或明显时

# 算法效率 Algorithm efficiency、
# O(1) - 常量时间 - 执行与输入无关-将总是花费相同的时间 | 在 Data Input-Time 坐标轴上是平行于 x 轴的直线
# O(n) - 线性时间 - 执行时间与输入大小成正比。完成时间随着输入大小的增加而增加
# O(log(n)) - 对数时间 - 完成时间与输入大小的对数成正比
# O(n^2) - 二次时间(Quadratic time) - 完成时间与输入大小的平方成正比

# 排序 Sorting
# 按有意义的顺序组织集合项目的过程
# - 数字顺序(上升或下降)
# - 字母顺序(A - Z)
# - 时间(最新，最旧)
# - 尺寸(最小，最大)
# - 价格(最便宜的，最贵的)
# 为了能够对集合中的项进行排序，我们必须有一种方法来相互比较项
# 排序是计算科学中研究得最透彻的问题
# 排序通常是一个单独的步骤，是另一个任务的一部分；对项的集合进行排序可以更容易地从集合中检索特定的项

# E.g. 在唱片收藏中找到特定的一首歌
# 设想 1 ：唱片未被排序
# 方法：
# 1. 随机选择一张唱片，并检查歌曲的标题
# 2. 重复，直到我选择正确的记录
# 结果：
# 最好的情况 O(1) - 我选择的第一张唱片就是我正在寻找的歌曲
# 最坏的情况 O(n) - 我选择的最后一张唱片是我正在寻找的歌曲(我必须搜索整个收藏)
# 设想 2 ：唱片以字母顺序排序
# 方法：
# 1. 从唱片集中间选择一条唱片，并检查歌曲的标题
# 2. 如果所选的唱片有我正在寻找的歌曲的标题，停止
# 3. 如果所选记录的歌曲的标题在字母顺序上低于我想要查找的歌曲，则丢弃所有在字母顺序上较高的记录(反之亦然)
# 4. 继续，直到找到正确的唱片
# 结果：
# 最好的情况 O(1) - 第一张选中的唱片就是我要找的歌
# 最坏的情况 O(log(n)) - 需要一直把收藏分成两半，直到找到正确的唱片

# 排序算法效率
# 任何算法的效率都与这些有关：
# 运行时间(Running time)：最好情况、平均情况、最坏情况
# 内存/空间(Menory / space)：要解决的问题的不同实例需要多少内存

# 排序方法：选择排序(Selection sort)、插入排序(Insertion sort)

# 搜索 Searching
# 检查列表或其他数据结构中的特定元素/项
# 通常有两种方法
# 顺序搜索 - 遍历数据结构并检查每个元素
# 区间搜索 - 算法是为搜索以某种方式排序的数据结构而设计的

# 线性搜索 Linear search
# 线性搜索 1
def linearSearch1(findMe, searchIn):
    for i in range(len(searchIn)):
        if searchIn[i] == findMe:
            return i
    return None

s = [2, 3, 4, 10, 40]
f = 10
print(linearSearch1(f,s))

# 线性搜索 2(while)
def linearSearch2(findMe, searchIn):
    i = 0
    while i < len(searchIn) and searchIn[i] != findMe:
        i += 1
    if i < len(searchIn):
        return i
    return None

s = [2, 3, 4, 10, 40]
f = 10
print(linearSearch2(f,s))

# 线性搜索效率
# 时间：
# - 最快时间 O(1) (第一位)
# - 平均时间 O(n) (与 n 成线性比例)
# - 最慢时间 O(n) (最后一位)
# 空间：
# - In place, O(1): a variable to store the element to be searched. 存储要搜索的元素的变量
print("")

# 二分搜索 Binary search - 递归 recursive
# 也被称为半区间搜索(half-interval search)
# 1. 对照列表中间的项检查搜索项
# 2. 如果列表中间的 item 等于搜索项，则返回它
# 3. 否则，如果搜索项大于中间项，则搜索项在列表的右半部分，丢弃左半部分并重复流程(右半部分转到 1 )
# 4. 否则，如果搜索项低于中间项，则搜索项在列表的左半部分，丢弃右半部分并重复流程(左半部分转到 1 )

def binarySearch(searchIn, findMe, start, end, step):
    # some additional output for clarity
    print(step, ": checking", searchIn[start:end + 1])
    if start > end:
        # start is the index we begin to check from, if it is greater than the last index to check up to, then findMe does not exist and we have checked all of searchIn
        print("Not found")
        return None
    
    # get the index of the middle item
    mid = (start + end) // 2
    # if findMe is in the middle, return it
    if findMe == searchIn[mid]:
        return mid

    # if findMe is less than the middle item
    if findMe < searchIn[mid]:
        # recursive call with only the left half of searchIn (start to item before the middle (mid - 1))
        return binarySearch(searchIn, findMe, start, mid - 1, step + 1)
    else:
        # recursive call with only the right half of searchIn (item after the middle (mid + 1) to end)
        return binarySearch(searchIn, findMe, mid + 1, end, step + 1)

s = [1, 3, 6, 14, 18, 23, 28, 40, 45, 49, 67, 68, 80]
f = 68
print("Index of", f, "is", binarySearch(s, f, 0, len(s), 0))

# 二分搜索效率
# 时间：
# - 最快时间 O(1)： 中间数
# - 平均时间 O(log(n))
# - 最慢时间 O(log(n))：极限情况
# 空间：
# - 迭代：O(1)
# - 递归：O(log(N)
# 二分搜索比线性搜索更高效