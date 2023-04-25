// 函数原型

// 函数先后关系
// 函数（如前面的 sum() 函数）应该在主函数 main 的上面
// 这是因为 C 的编译器自上而下分析你的代码

#include <stdio.h>

// 如果函数放在主函数的下面，编译时可能出现警告和错误
// C99 之前，C 语言会猜测函数的输入和返回类型（如猜测 sum() 的输入、输出是 int）
// 这时会出现警告

// void sum(int begin, int end) {...}
// 但实际上输出/返回值是 void， 与猜测有冲突

// 这时会出现错误
// 当然，根据编译器的不同，警告和错误可能不会出现

// 为了程序的美观我们希望程序的 main 函数在最上面
// 以 sum 为例，这时可以在 main 函数前插入：
// void sum(int begin, int end);
// 以分号结束，并将函数内的内容放置在后面，这样的编译不会出现问题
// 这一行称为函数的原型声明，函数内容部分称为函数定义

void sum(int begin, int end);       // 声明，原型声明中的参数（begin 和 end）可以省略，但最好保留（便于阅读）

int main()
{
    sum(1, 10);     // 这里会根据原型判断传入的参数类型是否正确
}

void sum(int begin, int end)        // 定义（实际的函数头）
{
    int i;
    int sum = 0;
    for (i = begin; i <= end; i++) {
        sum += i;
    }
    printf("%d 到 %d 的和是 %d\n", begin, end, sum);
    
    return;
}

// 而如果声明和定义前的返回类型不同（如声明是 int sum() 而定义是 void sum()），这样也会报错