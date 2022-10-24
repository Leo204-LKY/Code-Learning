// 第三周编程练习 1
// 输入北京时间 (BJT)，输出协调世界时 (UTC)
// UTC 相当于 BJT 减去 8
// 输入和输出均为四位数字，前两位和后两位分别为时和分
// 数字左侧的 0 省略，如 803 代表 8 时 3 分， 5 代表 0 时 5 分

#include <stdio.h>

int main()
{
    int bjt, utc;

    scanf("%d", &bjt);
    utc = bjt - 800;
    if (utc < 0)
    {
        utc += 2400;
    }

    printf("%d", utc);

    return 0;
}