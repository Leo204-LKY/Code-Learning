// 嵌套循环/多重循环

// 例：输出 100 以内的素数
// 基于 05-1 中的代码进行修改

#include <stdio.h>

int main() {
    int x;

    for(x = 2; x < 100; x++) {  // 第一层循环
        int i;
        int isPrime = 1; // x 是素数

        for (i = 2; i < x; i++) {  // 第二层循环
            if (x % i == 0) {
                isPrime = 0;
                break;
            }
        }

        if (isPrime == 1) {
            printf("%d ", x);
        }
    }
    printf("\n");

    return 0;
}

// 循环里面套循环即为嵌套的循环
// 可以是 for 、 while 或 do-while 嵌套，也可以相互嵌套
// 嵌套的层数无上限

// 但要注意：两个循环的控制变量不能相同（如本例中第一层变量是 x，第二层变量是 i ），若相同则会混淆