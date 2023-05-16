// 搜索
// 在一个数组中找到某个数的位置（或确认是否存在）

// 线性搜索
// 最基本的搜索方法是遍历

#include <stdio.h>

int search(int key, int a[], int len)
{
    int ret = -1;

    for (int i = 0; i < len; i++) {
        if (key = a[i]) {
            ret = i;
            break;
        }
    }

    return ret; // 单一出口原则
}

int main()
{
    int a[] = {1, 3, 2, 5, 12, 14, 23, 6, 9, 45};
    int r = search(12, a, sizeof(a) / sizeof(a[0]));
    printf("%d\n", r);

    return 0;
}