// 变量
// 在终端窗口中进行输入
// 输入以行为单位，行结束的标志是按下回车键。
// 按下回车键之前，程序不会读取到任何东西。

#include <stdio.h>

int main()
{
    int price = 0;  // 定义了一个变量，类型为 int 整数，初始值为 0
    // 也可在一行内定义多个变量： int a = 1, b = 2;
    // 但不可以这样赋值： int a, b = 1; ， 这样只会为 b 赋值 1
    // 等号代表把右边的值赋给左边的值
    // 在定义变量时赋值也称为初始化
    // 也可先不赋值（int amount, money;），但所有变量在第一次被使用（出现在赋值运算符=号右边）前都应被赋值一次
    // 注：C 语言中赋值和初始化差别不大，其他语言可能就有较大差别

    // 变量的名字是一种标识符
    // 基本原则：只能由字母、数字、下划线组成，数字不能作为第一位
    // C 语言的关键字（也称保留字）不能作为标识符
    // 不需要去背诵这些关键字，未来会有所认识；编译器也会告诉你错误

    // 等号是运算符，带有等号的式子称为表达式
    // C 语言是一种有类型的语言，所有变量使用前都必须定义或声明，且必须有确定的数据类型
    // 变量只能存放指定类型的数据，程序运行过程中不能改变变量的类型

    // 定义变量时，如果有小数就要用 double （双精度浮点数） ，用 int 则只会保留整数部分
    // 后续 scanf 中的 %d 也要改成 %lf

    printf("请输入金额（元）:");
    scanf("%d", &price);
    // & 代表对变量进行赋值（学习指针后会具体解释），如不加 & 则程序读不到变量
    // printf、scanf 的 f 是 formatted （格式化的）的意思

    // 对于 scanf ，出现在字符串中所有的东西都会被程序读取
    // %d 代表读取整数、%lf 代表读取浮点数

    int change = 100 - price;
    // 这里定义了第二个变量并且做了计算（这是 C99 的写法， C99 允许变量在任何地方定义变量）
    // 传统的 ANSI C 只能在代码开头定义变量，不能在代码中间定义

    // 100 是程序中固定不变的数，称为直接量(literal)
    // 更好的方式是定义一个直接量：
    // const int AMOUNT = 100;
    // 然后将式子中的 100 换为 AMOUNT （C99 写法）
    // （对于此类变量，习惯上用全大写）
    // 用有意义的名字便于其他人/自己理解这个数字的意义
    // 将 const 放在代码开头方便未来查找和修改
    // 变量一旦被 const 初始化，就不能再改变

    printf("找您 %d 元。\n", change);

    return 0;
}