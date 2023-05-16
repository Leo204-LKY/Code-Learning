// 第七周编程练习 1
// 多项式加法

// 读入两个多项式，然后输出这两个多项式的和
// 即把对应幂上的系数相加然后输出
// 要处理的最大幂为 100

#include <stdio.h>

int main()
{
    int polynomial[101] = {};
    int pow, coe; // power, coefficient
    int flag = 0;

    // 输入数据
    do {
        scanf("%d %d", &pow, &coe);
        polynomial[pow] += coe;

        if (pow == 0) {
            flag ++;
        }
    } while (flag < 2);

    // 判断最大幂次
    int maxpow = 0;
    for (int i = 0; i < 101; i++) {
        if (polynomial[i] != 0) {
            maxpow = i;
        }
    }

    // 输出数据
    for (int i = maxpow; i > 0; i--) {
        if (polynomial[i] != 0) {
            printf("%dx%d+", polynomial[i], i);
        }
    }
    printf("%d\n", polynomial[0]);

    return 0;
}