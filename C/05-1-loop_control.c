// 循环控制
// break 和 continue

// 素数：除 1 之外，只能被 1 和自己整除的数
// 如：2、3、5、7、11、13、17、19…
// 用户输入一个数，程序判断这个数是不是素数

// 基本思路：那这个数去除以一系列的数，判断是否能整除
// 显然需要循环，这种情况一般使用 for 循环

#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x);
    
    int i;
    int isPrime = 1;  // x 是素数

    for (i = 2; i < x; i++) {
        if (x % i == 0) {
            isPrime = 0;
            break;
            // 与前面学过的 switch-case 一样， break 语句会直接结束循环
            // 此外，还有 continue ，这个操作会跳过这一轮循环剩下的语句进入新的一轮循环
            // break 和 continue 对于 for 、 while 、 do-while 和 switch-case 都生效
        }
    }

    if (x == 1) {
        isPrime = -1;
    }

    if (isPrime == 1) {
        printf("是素数");
    } else if (isPrime == 0) {
        printf("不是素数");
    } else {
        printf("既不是素数也不是合数");
    }

    return 0;
}