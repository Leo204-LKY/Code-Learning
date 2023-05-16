// 二分搜索

// 线性搜索的问题在于没有效率
// 如果要搜索的元素在数组中靠后，那么程序几乎需要遍历数组
// 如果要搜索的元素不存在，程序需要遍历数组中的全部内容
// 对于含有大量数据（如几百万、几千万）的数组，这非常影响效率

// 如何提高效率？
// 将数组中的数据（如按从小到大的顺序）排好序，那么就可以用二分法进行查找
// | index |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 12 |
// | array |  2 |  4 |  7 | 11 | 13 | 16 | 21 | 24 | 27 | 32 | 36 | 40 | 46 |

// 从数组最中间的数字开始查找，如果目标数字就是中间数字，那么返回索引值
// 如果小于中间数字，就将范围限定到中间数字的左边，重复上面步骤
// 如果大于中间数字，就将范围限定到中间数字的右边，重复上面步骤

#include <stdio.h>

int binarySearch(int k, int a[], int len)
{
    int ret = -1;
    int left = 0;
    int right = len - 1;

    while (right > left)
    {
        int mid = (left + right) / 2;
        if (a[mid] == k)
        {
            ret = mid;
            break;
        } else if (a[mid] > k) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return ret;
}

int main()
{
    int a[] = {2, 4, 7, 11, 13, 16, 21, 24, 27, 32, 36, 40, 46};

    int index = binarySearch(11, a, sizeof(a) / sizeof(a[0]));
    printf("%d", index);
}

// 这样大大提高了搜索的效率，对于有 n 个元素的数组，最多只需要 log2(n) 次循环就可得出结果