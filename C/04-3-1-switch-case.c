// 多路分支

// 如果使用 if-else if 来判断各种情况，程序会从第一个 if 开始判断，直到找到成立的情况
// 而如果使用 switch-case ，则程序会直接跳到对应的 case 执行代码，直到遇到 break

#include <stdio.h>

int main()
{
    int type;
    scanf("%d", &type);
 
    // 对比使用 if-else if 和 switch-case 时程序的执行情况
    // 可以在下一行代码加入断点，逐步运行程序
    if (type == 1) {
        printf("你好\n");
    } else if (type == 2) {
        printf("早上好\n");
    } else if (type == 3) {
        printf("晚上好\n");
    } else if (type == 4) {
        printf("再见\n");
    } else {
        printf("啊，什么啊？\n");
    }

    // 可以在下一行代码加入断点，逐步运行程序
    switch ( type /* <控制表达式> */) {  // 这里的控制表达式 (即此处的 type) 只能为整数 int
        case 1/* <常量> */:  // 常量 (即此处的数字 1) 可以是常数，也可以是常数计算的表达式 (但表达式中所有的数均应为常数， C 99 Only)
            printf("你好\n");
            break;
        case 2:
            printf("早上好\n");
            break;
        case 3:
            printf("晚上好\n");
            break;
        case 4:
            printf("再见\n");
            break;
        default:
            printf("啊，什么啊？\n");
        // 注意： case 并不是划分各段的标志，不能阻止程序运行；而是一个入口，计算控制表达式的值后，程序会跳转到相匹配的 case 处
        // 如果上面的 case 不加 break ，则程序在执行完 case 中的代码后，会顺序运行到下面的 case/default ，直到遇到 break 或 switch 结束
        // 例：假设这个 switch 中的 break 全部不存在，则当 type == 1 时，会输出：你好\n 早上好\n 晚上好\n 再见\n 啊，什么啊？\n
        }

    return 0;
}