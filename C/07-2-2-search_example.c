// 搜索的例子

// 美元中多少分的货币有自己的名字
//  1 美分 penny
//  5 美分 nickel
// 10 美分 dime
// 25 美分 quarter
// 50 美分 half-dollar

// 假设需要一个程序，输入数字，输出这个数字以美分为单位对应的英文
// 如输入 10 ，输出 dime
// 可以通过散列表 hash table 来实现（数据结构课程中会学到）
// 如果没有学散列表，如何用 C 语言实现？

// 一个方案是数字和英文分别建立数组，而这两个数组相互对应
// | index | array 1 | array 2     |
// |     0 |       1 | penny       |
// |     1 |       5 | nickel      |
// |     2 |      10 | dime        |
// |     3 |      25 | quarter     |
// |     4 |      50 | half-dollar |
// 但是因为这是割裂的两个数组，在之后的学习中会有不便

// 在这个方案上改进，将两个数组合并为一个

#include <stdio.h>

struct {
    int amount;
    char *name
} coins[] = {
    {1, "penny"},
    {5, "nickel"},
    {10, "dime"},
    {25, "quarter"},
    {50, "half-dollar"}
};


int main()
{
    int k;
    scanf("%d", k);

    for (int i = 0; i < sizeof(coins) / sizeof(coins[0]); i++) {
        if (k == coins[i].amount) {
            printf("%s\n", coins[i].name);
            break;
        } 
    }

    return 0;
}