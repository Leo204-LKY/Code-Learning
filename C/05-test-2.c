// 第五周编程练习 2
// 输入范围为 [-100000,100000] 的整数，用拼音读出来，负号念作“fu”
// 每段拼音之间用空格分隔(最后的拼音后没有空格)

#include <stdio.h>

int main() {
    // 获取输入的数
    int x;
    scanf("%d", &x);

    // 判断是否为负数
    if (x < 0) {
        printf("fu ");
        x = - x;
    }

    // 获取整数的位数，确定 mask 的值
    int mask = 1;
    int d = x;
    while (d >= 10) {
        d /= 10;
        mask *= 10;
    }

    // 正序输出数字
    do {
        // 获取最大位
        int d = x / mask;
        // 判断最大位的值，输出拼音
        if (d == 0) {
            printf("ling");
        } else if (d == 1) {
            printf("yi");
        } else if (d == 2) {
            printf("er");
        } else if (d == 3) {
            printf("san");
        } else if (d == 4) {
            printf("si");
        } else if (d == 5) {
            printf("wu");
        } else if (d == 6) {
            printf("liu");
        } else if (d == 7) {
            printf("qi");
        } else if (d == 8) {
            printf("ba");
        } else {
            printf ("jiu");
        }

        // 去除最大位
        x %= mask;
        mask /= 10;
        
        // 判断是否为最后一位，不是则添加空格
        if (mask > 0) {
            printf(" ");
        }
    } while (mask > 0);

    printf("\n");
    return 0;
}