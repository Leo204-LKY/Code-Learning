// 求最大公约数
// 输入两个数 a 和 b ，输出它们的最大公约数
// 如输入 12 和 18 ，输出 6

// 有两种算法

// 第一种：枚举
// 1. 设 t 为 2
// 2. 如果 a 和 b 都能被 t 整除，则记下这个 t
// 3. t 加 1 后重复第二步，直到 t 等于 a 或者 b
// 4. 那么，曾经记下的最大的可以同时整除 a 和 b 的 t 就是它们的最大公约数

#include <stdio.h>

int main() {
    int a, b;
    int min;

    scanf("%d %d", &a, &b);
    if (a < b) {
        min = a;
    } else {
        min = b;
    }

    int ret = 0;
    int i;

    for (i = 1; i < min; i++) {
        if (a % i == 0) {
            if (b % i == 0) {
                ret = i;
            }
        }
    }
    // 第六周学到的逻辑运算可以简化这里两个嵌套的 if 以及前面的 if-else

    print("%d 和 %d 的最大公约数是 %d", a, b, ret);
}