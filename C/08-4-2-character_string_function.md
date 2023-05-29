# 字符串函数  
对于字符串， C 语言提供了很多函数来帮助处理  
下面这个函数是 C 语言标准库中的函数  
```C
#include <string.h>
```


## `<string.h>` 中的常用函数  
### `strlen`  
```C
size_t strlen(const char *s);
```
- 返回 `s` 的字符串长度（不包括结尾的 `\0`）  
- `const` 保证 `strlen` 不会修改字符串  

### `strcmp`  
```C
int strcmp(const char *s1, const char *s2);
```
- 比较两个字符串，返回：  
    - `0` ，如果 `s1 == s2`  
    - 正值，如果 `s1 > s2`  
    - 负值，如果 `s1 < s2`  
- 如果直接用 `s1 == s2` 进行比较，结果永远是 False ，因为它们的地址不同  
- 比较原理如下  
    1. 创建两个数组，将输入的字符串拆分成单个字符  
        | Index | 0 | 1 | 2 | 3 | 4 | ... |
        | --- | --- | --- | --- | --- | --- | --- |
        | s1 | a | b | c | `\0` | | |
        | s2 | a | B | c | ` `（空格） | `\0` | |
    2. 从 Index 0 开始比较两个数组中的元素所对应的 ASCII 编号（`\0` 编号为 0 ，` ` \[空格\]的编号为 32）  
        - 如果 s1 与 s2 不相等，返回编号 s1 - s2 的值  
        - 如果 s1 与 s2 相等，继续比较  
    3. 重复步骤 2，直到比较到两者均为 `\0` 或不相等时，返回对应的值（如果两个字符串相同，则返回 `0` ）  

### `strcpy`  
```C
char * strcpy(char *restrict dst, const char *restrict src);
```
- `cpy` 指 copy  
- 把 `src` 的字符串拷贝到 `dst`  
    - `restrict` 表明 `src` 和 `dst` 不重叠（C99）  
- 返回 `dst`  
    - 为了能链起代码  

### `strcat`  
```C
char * strcat(char *restrict s1, const char * restrict s2);
```
- 把 `s2` 拷贝到 `s1` 的后面，接成一个长的字符串  
- 返回 `s1`  
- `s1` 必须具有足够的空间  

### 安全问题  
`strcpy` 和 `strcat` 都可能出现安全问题：如果目的地没有足够的空间？  
因此，尽可能不要使用这两个函数  
安全的版本如下：  
```C
char * strncpy(char *restrict dst, const char *restrict src, size_t n);
char * strncat(char *restrict s1, const char *restrict s2, size_t n);
int strncmp(const char *s1, const char *s2, size_t n);
```
- 对于 `strncpy` 和 `strncat`  
    - 参数中多了一个 n，告知函数前面的字符串参数最大接受的字符数  
    - 超出上限的部分会被忽略  
- 对于 `strncmp`  
    - `n` 表示比较前 n 个字符是否相等，超出部分的字符会被忽略  
    - 并非为了安全  

### 字符串中找字符  
```C
char * strchr(const char *s, int c);
char * strrchr(const char *s, int c);
```
- 查找 `c` 在 `s` 中第一次出现的位置  
    - `strchr` 从字符串左侧开始查找  
    - `strrchr` 从字符串右侧开始查找  
- 返回 `NULL` 表示没有找到  