// 第四周 进一步的判断与循环

// 布尔类型 bool

#include <stdio.h>
#include <stdbool.h>
// 引入这个头文件之后就可以使用 bool 、 true 和 false

int main()
{
    bool b = 6 > 5;
    bool t = true;
    // 实际上引入的 bool 类型的值仍然是整数，因此想对这里的 t 赋值整数 2 也是可以的

    printf("%d\n", b);  // 这里实际上只会输出 1 ，而不是 true
    return 0;
}