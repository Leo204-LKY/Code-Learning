// 注释（comment）插入在代码中，用来向读者解释信息，便于理解
// 使用//会让程序忽略双斜杠后方至本行末尾的内容
// 这是 C99 中的注释， ANSI C 不支持

/*多行注释则可以使用本行开头和下行结尾的两个符号，
也可以用在一行代码中间*/
// 如： int ak = 47 /*36*/, y = 9
// 多行注释在 ANSI C 中就已支持


// 找零计算器
// 对 02-1-1 中的找零计算器进行优化，增加判断票面金额是否足够的功能，并添加注释

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
    }

    return 0;
}