// 使用数组做散列运算
// 写一个程序，输入数量不确定的 [0, 9] 范围内的整数，统计每一种数字出现的次数，输入 -1 表示结束

// 要不要记录每一个数字？
// 不需要，只需要记录每一个数字出现的次数

#include <stdio.h>

int main(void)
{
    const int number = 10;  // C99 可用
    int x;
    int count[number];
    int i;
    for (i = 0; i < number; i++) {
        count[i] = 0;
    }

    scanf("%d", &x);

    while (x != -1) {
        if (x >= 0 && x <= 9) {
            count[x] ++;
        }
        scanf("%d", &x);
    }

    for (i = 0; i < number; i++) {
        printf("%d:%d\n", i, count[i]);
    }

    return 0;
}