# 二维数组  

前面学习的是一维数组，实际上 C 语言支持二维甚至多维数组  
例：  
- ```C
    int a[3][5];
    ```
- 通常理解为 a 是一个 3 行 5 列的矩阵（考虑到其在计算机内的排列，通常认为第一个数字是行，第二个数字是列；这样与线性代数中的矩阵也是一样的排列方法）  
    | <!--  --> | <!--  --> | <!--  --> | <!--  --> | <!--  --> |
    | :-------: | :-------: | :-------: | :-------: | :-------: |
    | `a[0][0]` | `a[0][1]` | `a[0][2]` | `a[0][3]` | `a[0][4]` |
    | `a[1][0]` | `a[1][1]` | `a[1][2]` | `a[1][3]` | `a[1][4]` |
    | `a[2][0]` | `a[2][1]` | `a[2][2]` | `a[2][3]` | `a[2][4]` |

### 二维数组的遍历  
```C
for (i = 0; i < 3; i++) {
    for (j = 0; j < 5; j++) {
        a[i][j] = i * j;
    }
}
```
- `a[i][j]` 是一个 `int`  
- 表示第 i 行第 j 列上的单元  
- `a[i, j]` 在 C 语言中是运算符（逗号运算），等同于 `a[j]` ，而这不是正确的数组  

### 二维数组的初始化  
一维数组中可以用集合定义初始化，二维数组中也可以：  
```C
int a[][5] = {
    {0, 1, 2, 3, 4},
    {2, 3, 4, 5, 6},
};
```
- 列数必须是给出的，行数可以由编译器计算  
- 每行一个 {} ，逗号分隔  
- 最后的逗号可以存在（这是古老的传统）  
- 如果省略，表示补 0  
- C99 中，也可以用定位  

### 二维数组例： tic-tac-toe 井字棋游戏
- 读入一个 3 × 3 的矩阵，矩阵中的数字为 `1` 表示该位置上有一个 `X` ，为 `0` 表示为 `O`  
- 程序判断这个矩阵中是否有获胜的一方，输出表示获胜一方的字符 `X` 或 `O` ，或输出无人获胜  
```C
int main()
{
    const int size = 3;
    int board[size][size];
    int i, j;
    int numOfX;
    int numOfO;
    int result = -1;    // -1 - 没人赢； 1 - X 赢；0 - O 赢

    // 读入矩阵
    for (i = 0; i < size; i++) {
        for (j = 0; j < size; j++) {
            scanf("%d", &board[i][j]);
        }
    }

    // 检查行
    for (i = 0; i < size && result == -1; i++) {
        numOfO = numOfX = 0;
        for (j = 0; j < size; j++) {
            if(board[i][j] == 1) {
                numOfX++;
            } else {
                numOfO++;
            }
        }
        if ( numOfO == size ) {
            result = 0;
        } else if (numOfX == size) {
            result = 1;
        }
    }

    // 检查列
    if (result == -1) {
        for (j = 0; j < size && result == -1; j++) {
            numOfO = numOfX = 0;
            for (i = 0; i < size; i++) {
                if (board[i][j] == 1) {
                    numOfX++;
                } else {
                    numOfO++;
                }
            }
            if (numOfO == size) {
                result = 0;
            } else if (numOfX == size) {
                result = 1;
            }
        }
    }
    // 问题：检查行和列的代码相似，有没有可能可以合并起来？

    // 检查对角线
    if (result == -1) {
        numOfO = numOfX = 0;
        for (i = 0; i < size; i++) {
            if (board[i][i] == 1) {
                numOfX++;
            } else {
                numOfO++;
            }
        }
        if (numOfO == size) {
            result = 0;
        } else if (numOfX == size) {
            result = 1;
        }
    }
    if (result == -1) {
        numOfO = numOfX = 0;
        for (i = 0; i < size; i++) {
            if (board[i][size - i - 1] == 1) {
                numOfX++;
            } else {
                numOfO++;
            }
        }
        if (numOfO == size) {
            result = 0;
        } else if (numOfX == size) {
            result = 1;
        }
    }
    
    ...     // 输出结果
    return 0;
}
```
这个程序很好的演示了如何对一行或一列进行遍历，以及判断对角线等  