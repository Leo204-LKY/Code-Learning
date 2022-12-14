// 表达式
// 带有等号的一整行代码都称为表达式


// 算子(operand)
// 参与运算的值，可以为常数、变量、一个方法的返回值等


// 运算符(Operator)
// 进行运算的动作，如加法运算符+、减法运算符-、乘法运算符*、除法运算符/、取余%、括号()

// 优先级：与数学运算类似
// | 优先级 | 运算符 |   运算   | 结合关系 | 举例 |
// | 1     | +      | 单目不变 | 自右向左 | a*+b |
// | 1     | -      | 单目取负 | 自右向左 | a*-b |
// | 2     | *      | 乘       | 自左向右 | a*b |
// | 2     | /      | 除以     | 自左向右 | a/b |
// | 3     | +      | 加       | 自左向右 | a+b |
// | 3     | -      | 减       | 自左向右 | a-b |
// | 4     | =      | 赋值     | 自右向左 | a=b |
// *单目运算：只有一个变量参与（双目为两个，如 a + b 中的 a、b），如需要取 b 的相反数： -b
// 表中第一个是 a 乘以 +b ，第二个是 a 乘以 -b
// 赋值在 C 语言中也是运算，也有结果，如 a = b = 6 -> a = ( b = 6 ) ，计算机先会给 b 赋值 6 ，再给 a 赋值 b = 6（自右向左）
// (不推荐)嵌入式赋值： int c = 1 + ( b = a )，先给 b 赋值 a ， 在给 c 赋值 1 + b （不利于阅读，也容易产生错误，**不要用**)
// ↑ 不要用！

// 复合赋值：五个运算符（+、-、*、/、%）可以和赋值运算符（=）结合起来形成符合运算符
// total += 5 即 total = total + 5
// total *= sum + 12 即 total = total * (sum + 12)
// 程序会先将右侧计算完毕后再进行复合赋值计算
// 注意复合赋值两个符号中间不能有逗号

// 递增/递减运算符
// ++ 和 -- 是两个特殊运算符，会让变量 +1 或 -1
// 可以放在变量前面或后面（但表达式中， a++ 的值是 a + 1 以前的值，而 ++a 的值是 a + 1 以后的值）
// count++ 即 count += 1
// 例：
// >> a = 10;
// >> printf("a++ = %d\n", a++);       // 输出：10
// >> printf("a = %d\n", a)            // 输出：11
// >> printf("++a = %d\n", ++a);       // 输出：12
// >> printf("a = %d\n", a);           // 输出：12

// 复合赋值、递增/递减运算符可以单独使用，但和嵌入式赋值一样，不要放进表达式


// 例：计算时间差

#include <stdio.h>

int main()
{
    int hour1, minute1;
    int hour2, minute2;

    scanf("%d %d", &hour1, &minute1);
    scanf("%d %d", &hour2, &minute2);

    int t1 = hour1 * 60 + minute1;
    int t2 = hour2 * 60 + minute2;

    int t = t2 - t1;

    printf("时间差是 %d 小时 %d 分。\n", t / 60, t % 60);
    // t / 60 ：小时部分，t % 60 ：分钟部分

    return 0;
}