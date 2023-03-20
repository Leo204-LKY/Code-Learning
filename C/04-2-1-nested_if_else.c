// 嵌套的 if-else

// 例：判断三个数的大小

#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int max = 0;

    if (a > b) {
        if(a > c) {
            max = a;
        } else {
            max = c;
        }
    } else {
        if (b > c) {
            max = b;
        } else {
            max = c;
        }
    }

    printf("The max is %d\n", max);
    return 0;
}

// 当 if 的条件满足或者不满足的时候要执行的语句也可以是一条 if 或 if-else 语句，这就是嵌套的 if 语句
// else 总是和最近的那个 if 匹配
// 尽管只有一行时 if/else 可以不用 {} ，但是最好要加上