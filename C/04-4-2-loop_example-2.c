// 算平均数
// 让用户输入一系列的正整数，最后输入 -1 表示输入结束，然后程序计算出这些数字的平均数，输出输入的数字的个数和平均数

// 写一个程序的基本步骤：变量 -> 算法 -> 流程图 -> 程序

// 1. 变量
// 一个记录读到的整数的变量
// 平均数怎么算？
//   只需要读到每一个数，就把它加到一个累加的变量里，把全部数据读完，再拿它去除以得到的数的个数即可
// 一个变量记录累加的结果，一个变量记录读到的数的个数

// 2. 算法
// i.   初始化变量 sum 和 count 为 0
// ii.  读入 number
// iii. 如果 number 不是 -1 ，则将 number 加入 sum ，并将 count 加 1 ，回到 ii
// iv.  如果 number 是 -1 ，则计算和打印出 sum / count （注意换成浮点来计算）

// 3. 流程图
// 略

// 4. 程序
#include <stdio.h>

int main()
{
    int number;
    int sum = 0;
    int count = 0;

    // do
    // {
    //     scanf("%d", &number);
    //     if (number != -1)
    //     {
    //         sum += number;
    //         count ++;
    //     }
    // } while (number != -1);
// 使用上面这种代码，每次循环需要进行两次 number != -1 的判断

// 能不能只用一次呢？
    scanf("%d", &number);
    while (number != -1) {
        sum += number;
        count ++;
        scanf("%d", &number);
    }
// 尽管上面用了两次 scanf ，但第一个 scanf 只会执行一次，会比原来的合理

    printf("%f\n", 1.0 * sum / count);

}

// 编写程序时不同方式的选择，影响了程序的优劣、运行速度、他人理解的难易程度