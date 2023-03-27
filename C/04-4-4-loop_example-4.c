// 整数求逆
// 输入一个正整数，输出逆序的数
// 结尾 0 的处理

// 一个整数是由 1 至多位数字组成的，如何分解出证书的各位上的数字，然后加以计算
// 对一个整数做 %10 的操作，就得到它的个位数
// 对一个整数做 /10 的操作，就去掉了它的个位数
// 再对上一个操作的结果做 %10 ，就得到原来这个数的十位数了；以此类推

#include <stdio.h>

int main()
{
    int x;
    scanf("%d", &x);
    
    int digit;
    int ret = 0;

    // 假设需要 700 输出 007
    while (x > 0) {
        digit = x % 10;
        printf("%d", digit);
        ret = ret * 10 + digit;
        printf("x = %d, digit = %d, ret = %d\n", x, digit, ret);   // 调试输出，调试完毕后应该注释掉
    }

    // printf("%d", ret);  // 假设需要 700 输出 7，取消注释本行然后注释掉 23 行

    return 0;
}

