# 字符串常量  
假设我们要运行这段代码：  
```C
char* s = "Hello World";
s[0] = 'B';

printf("Here!s[0] = %c\n", s[0]);
```
编译时不会出现任何问题，但运行时程序会报错（`s[0] = 'B';` 行出现 `Segmentation fault`），后面的 `printf()` 也完全不会输出  

再看看这段代码：  
```C
char *s = "Hello World";
char *s2 = "Hello World";

printf("s  = %p\n", s);
printf("s2 = %p\n", s2);
printf("Here! s[0] = %c\n", s[0]);
```
运行的输出为：  
```
s  = 0x67f8e
s2 = 0x67f8e
Here! s[0] = H
```
说明 `s` 和 `s2` 指向了相同的地址，且这个地址很小（相比之下，如果为程序定义一个本地变量 `int i = 1;` ，这个变量的地址会比较大 \[在这里比 `s` 和 `s2` 多三位\]）  
这个很小的地址，实际上位于程序的代码段，并且它是只读的  
因此前面在给字符串赋值时，程序会保护性地报错  

## 字符串常量  
```C
char* s = "Hello World";
```
- `s` 是一个指针，初始化为指向一个字符串常量  
    - 由于这个常量所在的地方，所以实际上 `s` 是 `const char* s;` ，但是由于历史遗留原因，编译器接受不带 `const` 的写法  
    - 但是试图对 `s` 所指的字符串做写入会导致严重的后果  
- 如果需要修改字符串，应该用数组  
    ```C
    char s[] = "Hello World";
    ```
    - `*s` 说明是指针，要指向某一个地址  
    - `s[]` 说明是字符串，只会在这个变量所在的地址  

## 指针还是数组？  
当我们需要程序中有一个字符串的时候，选择指针还是数组？
```C
char *str = "Hello";
char word[] = "Hello";
```
- **数组**：这个字符串就在这里  
    - 作为本地变量空间，程序结束后会被自动回收  
- **指针**：这个字符串不知道在哪里  
    - 处理参数  
        对于函数中的参数，数组和指针没有区别，因此可以用指针来处理参数  
    - 动态分配空间  

根据以下原则选择：  
- 要构造一个字符串 → **数组**  
- 要处理一个字符串 → **指针**  

## `char*` 就是字符串？  
这个说法**❌不正确**，或者说不准确  
- 字符串可以表达为 `char*` 的形式，但  
- `char*` 不一定是字符串  
    - 本意是指向字符的指针，可能指向的是字符的数组（就像 `int*` 一样）  
    - 只有它所指的字符数组有结尾的 `'0'` （或 `\0`），才能说它所指的是字符串  