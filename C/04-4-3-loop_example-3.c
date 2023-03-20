// 猜数游戏
// 计算机来想一个数，让用户来猜。用户每输入一个数，就告诉 Ta 是大了还是小了，直到用户猜中为止。最后还要告诉用户 Ta 猜了多少次

// 因为需要不断让用户猜，所以需要用到循环
// 在实际写出程序前，我们可以先用文字描述程序的思路
// 核心重点是循环的条件（人们往往会考虑循环终止的条件）

// 随机数： rand()，每次召唤就会得到一个随机的整数

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
// stdlib.h 、 time.h 和对应的代码之后会学习

int main()
{
    srand(time(0));
    int number = rand() % 100 + 1;
    // 现在只需要知道这两行会求得平均数
    // rand() 生成的数会非常大，因此使用取余(% 100)来将取得的随机数控制在 100 以内
    int count = 0;
    int a = 0;

    printf("我已经想好了一个 1 到 100 之间的数。");

    do
    {
        printf("猜猜这个 1 到 100 之间的数：");
        scanf("%d", &a);
        count++;

        if (a > number)
        {
            printf("你猜的数大了。");
        }
        else if (a < number)
        {
            printf("你猜的数小了。");
        }
    } while (a != number);

    printf("太好了，你用了 %d 次就猜到了答案。\n", count);
    return 0;
}