// 排序初步
// 选择排序

// 二分法效率很高
// 但如果数组是无序的，该怎么给这个数组排序？

int max(int a[], int len)
{
    int maxid = 0;
    for (int i = 1; i < len; i++) {
        if (a[i] > a[maxid])
        {
            maxid = i;
        }
    }
    return maxid;
}

int main()
{
    int a[] = {2, 45, 6, 12, 87, 34, 90, 24, 23, 11, 65};
    int len = sizeof(a) / sizeof(a[0]);
    int maxid = max(a, len);
}