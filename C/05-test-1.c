// 第五周编程练习 1
// 给定两个整数 n 和 m ， 0<n<=m<=200 ，输出第 n 个素数到第 m 个素数之间所有素数的和，包含 n 和 m 

#include <stdio.h>

int main()
{
    int n, m;
    int total = 0;
    int cnt = 1;
    int num = 2;
    scanf("%d %d", &n, &m);

    // 判断一个数是否是质数
    while (cnt <= m) {
        int isPrime = 1;

        for (int i = 2; i < num; i++) {
            if (num == 2) {
                break;
            } else if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }

        if (isPrime == 1) {
            if (cnt >= n) {
                total += num;
            }
            cnt += 1;
        }

        printf("num = %d, cnt = %d, count = %d\n", num, cnt, total);
        num += 1;
    }
    printf("%d", total);
    return 0;
}