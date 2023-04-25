// 从函数中返回

// return 很早就出现了：主程序最后的 return 0;
// 其停止函数的执行，并返回一个值/表达式的值（如有，变量也是一种表达式）
// 或者直接使用 return; 而不加变量，这样会停止函数的执行，但不返回值

#include <stdio.h>

int max(int a, int b)
// 返回类型 int 表示这个函数会返回整数值
{
    int ret;
    if (a > b) {
        ret = a;
    } else {
        ret = b;
    }

    return ret;
    // 这个变量也可以用其他命名
    // 甚至不使用变量，直接在 if-else 语句中使用 return a/b; 也可以
    // 但根据 C 语言的单一出口原则，一个函数中应该只有一个 return （可以有多个，但不好）
}

// 函数中返回的值可以赋值给变量
// a = max(1, 2);
// 可以再传递给函数
// a = max(max(2, 3), 4)
// 甚至可以丢弃
// max(22, 33)
// 因为有些时候并不需要函数返回的结果，而是其过程（如输出等）

// 如果函数不返回值，那么返回类型应该是 void
void sum(int begin, int end)
{
    int i;
    int sum = 0;
    for (i = begin; i <= end; i++) {
        sum += i;
    }
    printf("%d 到 %d 的和是 %d\n", begin, end, sum);
    
    return;
    // 最后这个 return 不能带值
    // 或者直接省略 return
    // 调用时不能做返回值的赋值
}