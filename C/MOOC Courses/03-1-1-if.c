// if 语句
// 判断机制，满足条件时执行

// 以上讲中的计算时间差为例，可以改为

#include <stdio.h>

int main()
{
    int hour1, minute1;
    int hour2, minute2;

    scanf("%d %d", &hour1, &minute1);
    scanf("%d %d", &hour2, &minute2);

    int ih = hour2 - hour1;
    int im = minute2 - minute1;
    if ( im < 0 ) {
    // 当 im 的值为负数时执行下列{}中的语句
    // 不满足时跳过，进入执行后续printf语句
        im = 60 + im;
        ih --;
    }

    printf("时间差是 %d 时 %d 分。", ih, im);
    return 0;
}