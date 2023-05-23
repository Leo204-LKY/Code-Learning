# 指针与数组  
为什么数组传进函数以后 sizeof() 就不对了？  

## 传入函数的数组成了什么？  
上一节中讲到，传入函数的参数（如 int）只是它的值，如果是指针则传入的是地址，那么数组传入函数后变成了什么？  
为什么不能在函数内用 sizeof() 来判断数组中元素的个数？  
### 以判断数组最大最小值为例
```C
#include <stdio.h>

void minmax(int a[], int len, int *max, int *min);

int main(void)
{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 16, 17, 21, 23, 55,};
    int min, max;
    // 在主函数和 minmax 函数中进行测试，加入 printf 输出数组 a[] 的大小
    printf("main sizeof(a[]) = %lu\n", sizeof(a));

    minmax(a, sizeof(a) / sizeof(a[0]), &min, &max);
    printf("min = %d, max = %d\n");

    return 0;
}

void minmax(int a[], int len, int *max, int *min)
{
    int i;
    printf("minmax sizeof(a[]) = %lu\n", sizeof(a));
    *min = *max = a[0];
    for (i = 1; i < len; i++) {
        if (a[i] < *min) {
            *min = a[i];
        }
        if (a[i] > *max) {
            *max = a[i];
        }
    }
}
```
- 实际输出可以得到，主函数中 a[] 的大小是 68，而在 minmax 函数中 a[] 的大小只有 8 （64 位架构下）  
    - 这个大小与 64 位架构下一个指针的大小一样  
- 在编译时弹出的警告如下：  
    - `'sizeof' on array function parameter 'a' will return size of 'int *' [-Wsizeof-array-argument]`  
    在数组函数内的参数 a 上， sizeof 会返回 'int *' 的大小（而不是 'int []' 的大小）
- 换句话说，函数参数内的数组其实是一个指针 int *，函数内的数组与主函数的数组就是一个数组  
    - 因此无法在函数内使用 sizeof() 获取到一个数组的大小  


## 函数参数表中的数组实际上是指针  
- `sizeof(a) == sizeof(int *)`  
- 但是可以用数组的运算符进行运算  
    - 把 `void minmax(int a[], int len, int *max, int *min)` 中的 `a[]` 改成 `*a` ，即便在函数中将这个变量当作数组来用（如 `a[0]`, `a[i]`），编译和运行都不会出问题  

### 以下四种函数的原型是等价的：  
- `int sum(int *ar, int n);`  
- `int sum(int *, int);`  
- `int sum(int ar[], int n);`  
- `int sum(int [], int);`  
* 注意，不是说这种函数的类型是等价的，只是说在参数表中是等价的  

### 实际上，数组变量是特殊的指针  
- 数组变量本身表达地址，所以  
    - `int a[10];` 和 `int *p = a;` 无需用 `&` 取地址  
    - 但数组的单元 `a[i]` 表达的是变量，需要用 `&` 取地址  
    - `a == &a[0]`  
- `[]` 运算符可以对数组做，也可以对指针做  
    - `p[0]` <==> `a[0]`  
- `*` 运算符可以对指针做，也可以对数组做  
    - `*a = 25;`  
- 实际上，数组变量是 const 的指针，所以不能被赋值  
    - `int a[]` <==> `int * const a = ...`  
    - 也就是不能用 `int b[] = a;` 来给数组 `b` 赋值的原因  