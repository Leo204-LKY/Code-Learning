// 循环的例子

// 编程的难度在于如何把问题变为程序

// 例：计算 log 2 x 的近似值

#include <stdio.h>

int main()
{
    int x;
    int ret = 0;

    scanf("%d", &x);
    while (x > 1) {
        x /= 2;
        ret ++;
    }
    printf("log2 of %d is %d\n", x, ret);
// 假设输入 64，最终的输出为： log 2 of 1 is 6
// 因为 x 的值在编程时有变化，因此应该引入一个新的变量存储原始值
// 这是写程序中的一个小套路

// 但是这些值是怎么定的？
// 可不可以用 do-while 循环？
// 为什么 ret 的初始值是 0 ？为什么条件是 x > 1 ？
// 通过分析解决这些问题
// 例如， ret 初始值可以为 0 ，条件也相应地变为 x > 0
// 这样也能得出正确答案

// 所以编程中没有标准答案，一定有多种方法可以实现要求

// 再例如：计数循环
    int count = 100;
    while (count >= 0) {
        count --;
        printf("%d\n", count);
    }
    printf("发射！\n");
// 想要知道这个循环执行的次数（ 100 次还是 101 次？）、循环停下来时有没有输出最后的 0 、循环结束后 count 的值是多少？
// 可以在纸面模拟，也可以进入 debug 一步一步过
// 但是这里有 100+ 次循环，非常麻烦
// 因此，如果要模拟一个很大次数的循环，可以模拟较少的循环次数，然后做出推断
// 这也是一个小套路

// 以上面的计数循环为例，将 count 设为 3 ，模拟/debug 查看结果，获得答案
// 循环走了 4 轮， 0 有输出（最后输出的数为 -1），循环结束时 n = -1
// 再据此对程序进行修改

    return 0;
}