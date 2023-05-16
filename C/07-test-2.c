// 第七周编程练习 2
// 鞍点

// 给定一个 n*n 矩阵 A。矩阵 A 的鞍点是一个位置（i，j），在该位置上的元素是第 i 行上的最大数，第 j 列上的最小数。一个矩阵 A 也可能没有鞍点
// 你的任务是找出 A 的鞍点

// 输入的第 1 行是一个正整数n, （1<=n<=100），然后有 n 行，每一行有 n 个整数，同一行上两个整数之间有一个或多个空格
// 对输入的矩阵，如果找到鞍点，就输出其下标。下标为两个数字，第一个数字是行号，第二个数字是列号，均从0开始计数
// 如果找不到，就输出 NO
// 题目所给的数据保证了不会出现多个鞍点

#include <stdio.h>

#define MAX_SIZE 100

int main()
{
    int n;
    scanf("%d", &n);

    int matrix[MAX_SIZE][MAX_SIZE] = {};
    int maxrow[MAX_SIZE] = {};  // 行
    int mincol[MAX_SIZE] = {};  // 列
    int saddlerow = -1;
    int saddlecol = -1;

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            scanf("%d", &matrix[row][col]);
        }
    }

    // 查找某一行最大数
    for (int row = 0; row < n; row++) {
        maxrow[row] = 0;
        for (int col = 1; col < n; col++) {
            if (matrix[row][col] > matrix[row][maxrow[row]]) {
                maxrow[row] = col;
            }
        }
    }

    // 查找某一列最小数
    for (int col = 0; col < n; col++) {
        mincol[col] = 0;
        for (int row = 1; row < n; row++) {
            if (matrix[row][col] < matrix[mincol[col]][col]) {
                mincol[col] = row;
            }
        }
    }

    // 查找鞍点
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (row == mincol[col]) {
                if (col == maxrow[row]) {
                    saddlerow = row;
                    saddlecol = col;
                }
            }
        }
    }

    if (saddlecol != -1) {
        printf("%d %d\n", saddlerow, saddlecol);
    } else {
        printf("NO\n");
    }

    return 0;
}