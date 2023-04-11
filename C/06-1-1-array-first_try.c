// 初试数组

// 循环样例 2 (04-4-2-loop_example-2.c) 中完成了下面的要求：
// 如何写一个程序计算用户输入的数字的平均数？
// 其中的实现方法不需要记录输入的每一个数

// 但如果修改要求：
// 如何写一个程序计算用户输入的数字的平均数，并输出所有大于平均数的数？
// 这个代码又该如何实现？

// 如何记录很多个数？
// 用 int num1, num2, num3...？
// 这样肯定是不可行的

#include <stdio.h>

int main()
{
    int x;
    double sum = 0;
    int cnt = 0;
    int number[100];        // 定义数组
                            // 上一行定义了一个名为 number 的变量，这个变量就是数组，可以存 100 个整数
                            // 数组类似 Python 中的列表，但也有一些区别

    scanf("%d", &x);
    while (x != -1) {
        number[cnt] = x;    // 对数组中的元素赋值
                            // 只要 x 不等于 -1 ，设置 number 数组中第 cnt 位(cnt 从 0 开始)的值为 x
        sum += x;
        scanf("%d", &x);
    }

    if (cnt > 0) {
        print("&f\n", sum / cnt);
        int i;
        for (i = 0; i < cnt; i++) {
            if (number[i] > sum / cnt) {    // 使用数组中的元素
                printf("%d\n", number[i]);  // 遍历数组
            }
        }
    }
}

// 这个程序存在安全隐患，因为这个数组只能容纳 100 个元素，程序没有判断 cnt 是否会超过容量的步骤