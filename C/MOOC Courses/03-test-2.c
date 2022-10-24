// 第三周编程练习 2
// n 名学生按 1、2、1、2… 的顺序报数，报 1 的为第一列，报 2 的为第二列
// 输出那些同学被分到第一列，用空格分隔(最后一个数字后没有空格)

#include <stdio.h>

int main()
{
    int n, i;
    i = 1;
    scanf("%d", &n);

    while (i < n - 1)
    {
        printf("%d ",i);
        i += 2;
    }

    printf("%d", i);

    return 0;
}