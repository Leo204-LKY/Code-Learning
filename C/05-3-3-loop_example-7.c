// 正序分解整数
// 输入： 13425
// 输出： 1 3 4 2 5

#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x);

    do {
        int d = x % 10;
        printf("%d", d);
        if (x >= 10) {
            printf(" ");
        }
        x /= 10;
    } while (x > 0);

    printf("\n");
    return 0;
}