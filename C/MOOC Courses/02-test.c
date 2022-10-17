// 第二周编程练习
// 输入一个三位数，输出逆序的数

#include <stdio.h>

int main()
{
    int in, num1, num2, num3, out;

    scanf("%d", &in);

    num1 = in / 100;
    num2 = (in - num1 * 100) / 10;
    num3 = in % 10;

    out = num1 + num2 * 10 + num3 * 100;
    printf("%d", out);

    return 0;
}