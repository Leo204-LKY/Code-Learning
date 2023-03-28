// 第四周编程练习 2
// 对数字求奇数特征值
// 对于一个整数，从个位开始对每一位数字编号，个位是 1 号，十位是 2 号，以此类推。这个整数在第 n 位上的数字记作 x ，如果 x 和 n 的奇偶性相同，则记下一个1 ，否则记下一个 0 。按照整数的顺序把对应位的表示奇偶性的 0 和 1 都记录下来，就形成了一个二进制数字。比如，对于 342315，这个二进制数字就是 001101。
// 你的程序要读入一个非负整数，整数的范围是[0,1000000]，然后按照上述算法计算出表示奇偶性的那个二进制数字，输出它对应的十进制值

#include <stdio.h>

int main() {
    int num, digit, power;
    int power_result = 1;
    int bit = 0;
    int binary = 0;

    scanf("%d", &num);

    while(num > 0) {
        bit ++;
        digit = num % 10;
        num = num / 10;

        if (bit % 2 == digit % 2) {
            power = bit - 1;
            while (power > 0) {
                power_result *= 2;
                power -= 1;
            }
            binary += power_result;
            power_result = 1;
        }
    }

    printf("%d", binary);

    return 0;
}