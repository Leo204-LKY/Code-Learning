// 求最大公约数
// 输入两个数 a 和 b ，输出它们的最大公约数(gcd)
// 如输入 12 和 18 ，输出 6

// 有两种算法

// 第二种：辗转消除法
// 1. 如果 b 等于 0 ，计算结束， a 就是最大公约数
// 2. 否则，计算 a 除以 b 的余数 t ，让 a 等于 b ，而 b 等于 t
// 3. 回到第一步

// E.g.:
// a   b   t
// 12  18  12
// 18  12  6
// 12  6   0
// 6   0   0

#include <stdio.h>

int main() {
    int a, b;
    int t;
    
    scanf("%d %d", &a, &b);

    while (b != 0) {
        t = a % b;
        a = b;
        b = t;
    }

    printf("gcd = %d\n",a);

    return 0;
}