// 对 02-1-1 和 03-1-2 中的找零计算器再进行优化
// 当票面不够时，应该用 else

#include <stdio.h>

int main()
{
    // 初始化
    int price = 0;
    int bill = 0;

    // 读入金额和票面
    printf("请输入金额：");
    scanf("%d", &price);
    printf("请输入票面：");
    scanf("%d", &bill);
    //计算找零
    if ( bill >= price ) {
        printf("应该找您：%d\n", bill - price);
    } else {
        printf("你的钱不够\n");
    }
}

// 当 if 中的条件不成立时，将执行 else 中的程序

// 如果需要继续进行判断，则可以添加 else if （否则如果）并在后面的括号中输入判断条件
// >> if ( a > b ) {
// >>     printf("a 比 b 大\n");
// >> } else if ( a < b ) {
// >>     printf("a 比 b 小")   
// >> } else {
// >>     printf("a 与 b 大小相同")
// >> }

// if 、 else if 和 else 后可以不用 {} 而是只有一个语句
// >> if ( total > amount )
// >>     total += amount + 10;
// 第二行中的分号才表示 if 语句结束
// 但如果 if 后需要跟多行语句，则仍需要 {}

// 程序不必要追求最短，应该让足够多的人尽可能读懂你的代码
