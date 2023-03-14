# Lecture 4.2: Recursion 递归

# 递归模式允许重复
# 当一个方法调用自己时成为递归
# 典例：阶乘函数 factorial function - n!
def factorial(n):
    if n == 0:
        print("n == 0")
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

# sample usage
print(factorial(5))
print()


# 递归消除了嵌套循环和复杂的案例分析
# 递归使代码更具可读性，从而使其更易于维护
# 如果代码可读性更好，那么 bug 潜伏的地方就更少
# 如果代码可读性更强，那么测试也会变得更容易


# Content of a Recursive Method递归方法的内容
# - Base case(s) 基本情况
#   - 不执行递归调用的输入变量的值被称为基本情况(至少应该有一个基本情况)
#   - 每个可能的递归调用链最终都必须到达一个基本情况
# - Recursive calls 递归调用
#   - 调用当前方法
#   - 每个递归调用都应该被定义为朝着基本情况前进

# 每次函数调用都会创建一个帧(frame, 或 activation record 激活记录)来存储关于函数调用的信息。这些在递归中一直向下直到再次向上
# 递归跟踪
# - 用于每个递归调用的方框
# - 从每个调用方到被调用方的箭头
# - 从每个被调用方到调用方的箭头显示返回值


# English Ruler Example
def draw_line(tick_length, tick_label = ""):
    '''Draw one line with given tick length (followed by optional label)'''
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)

def draw_interval(center_length):
    '''Draw tick interval based upon a central tick length'''
    if center_length > 0:                   # stops when length drops to 0
        draw_interval(center_length - 1)    # recursively draw top ticks
        draw_line(center_length)            # draw center tick
        draw_interval(center_length - 1)    # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    '''Draw English ruler with given number of inches and major tick length'''
    draw_line(major_length, "0")            # draw inch - line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)     # draw interior ticks of inch
        draw_line(major_length, str(j))     # draw inch j line and label

# sample use
draw_ruler(5, 3)


# Computing Fibonacci Numbers 计算斐波那契数列
# F(0) = 0, F(1) = 1, F(i) = F(i-1) + F(i-2) for i > 1
# Algorithm BadFib(k):
#     Input: Nonnegative integer k
#     Output: The kth Fibonacci number F(k)
#   if k = 1 then
#       return k
#   else
#       return BadFib(k - 1) + BadFib(k - 2)
# 这个算法不好，因为最后调用了两次

# 通过分析可以得知，每隔一段时间，n(k)至少会增加一倍，即n(k) > 2^(k/2)。它是指数级的!
# 据此优化算法
# Algorithm LinearFibonacci(k):
#     Input: A nonnegative integer k
#     Output: Pair of Fibonacci numbers (F(k) , F(k-1))
#   if k = 1 then
#       return (k, 0)
#   else
#       (i, j) = LinearFibonacci(k - 1)
#   return (i + j, i)
# 我们保留先前的值并将其传递给下一次调用以供使用，LinearFibonacci 进行 k-1 次递归调用


# Linear Recursion 线性递归
# 基本情况(base case(s))的测试
# - 首先测试一组基本情况(至少应该有一个)
# - 每一个可能的递归调用链最终都必须到达一个不使用递归的基本情况
# 复发一次(recur once)
# - 执行单个递归调用
# - 这一步可能有一个测试，决定进行几个可能的递归调用中的哪一个，但它最终应该只进行这些调用中的一个
# - 定义每个可能的递归调用，使其朝着基本情况前进
# E.g.:
# 1. 计算数组前 n 项的和
# Algorithm LinearSum(S, n):
#     Input: A integer array S and an integer n = 1, such that S has at least n elements
#     Output: The sum of the first n integers in S
#   if n == 0 then
#       return 0
#   else
#       return LinearSum(S, n - 1) + S[n - 1]
#
# 2. 反转数组
# Algorithm ReverseArray(A, start stop):
#     Input: An array A and nonnegative integer indices start and stop
#     Output: The reversal of the elements in A starting at index stop and ending at stop
#   if start < stop -1 then
#   Swap A[start] and A[ stop]
#   ReverseArray(A, start + 1, stop- 1)
#   return
# 在创建递归方法时，以方便递归的方式定义方法是很重要的。这有时需要我们定义传递给方法的附加参数，以满足基本情况。例如，我们将数组反转方法定义为 ReverseArray(A, i, j)，而不是 ReverseArray (A)。
def reverse(S, start, stop):
    '''Reverse elements in implicit slice S[start:stop]'''
    if start < stop - 1:                                # if at least 2 elements
        S[start], S[stop - 1] = S[stop - 1], S[start]   # swap first and last
        reverse(S, start + 1, stop - 1)                 # recur on rest