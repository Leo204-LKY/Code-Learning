// 第 4 周编程练习 1
// 输入一系列范围为 (0, 100000) 的正整数，以 -1 结束，程序输出奇数和偶数的个数

#include <stdio.h>

int main() {
    int num = 0;
    int even = 0;
    int odd = 0;

    scanf("%d", &num);
    while (1){
        scanf("%d", &num);
        if (num == 0) {
            break;
        }

        if (num % 2 == 0) {
            even ++;
        } else {
            odd ++;
        }
    }

    printf("%d %d", odd, even);
}