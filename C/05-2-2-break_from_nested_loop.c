// 从嵌套的循环中跳出

// 例：用 1 角、 2 角和 5 角硬币凑出 10 元以下的金额

#include <stdio.h>

int main() {
    int x;
    int one, two, five;

    scanf("%d", &x);
    for (one = 1; one < x * 10; one++) {
        for (two = 1; two < x * 10 / 2; two ++) {
            for (five = 1; five < x * 10 / 5; five++) {
                if (one + two * 2 + five * 5 == x * 10) {
                    printf("可以用 %d 个 1 角， %d 个 2 角和 %d 个 5 角得到 %d 元\n", one, two, five, x);
                    // 如果我们只需要它算出一个结果就退出循环，要怎么做？
                    // 只加一个 break 话，其只会跳出最内层的一个循环
                    // continue 也是如此，只能对他所在的这一个循环生效

                    // 一个方法是添加变量(exit)，由最内层控制，在每层循环末添加 if {break;} 语句，条件成立(exit == 1)时执行 break
                    // 另一种方法是 goto
                    goto out;
                    // goto 后加入自定义的标号，会将代码跳到标号(这里是 out)所在位置
                }
            }
        }
    }
out: // <- 跳到这里，格式为自定义的标号+冒号
    return 0;
}

// goto 在历史上名声不好，因为它破坏了程序的结构性，可以让程序不按代码顺序执行，因此有的教材不会教这个
// 但实际上 goto 在某些场合（目前只需要直到本例中的多重循环，其他地方不要使用）使用十分方便