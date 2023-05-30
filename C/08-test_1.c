// 第八周编程练习 1
// 要读入一行文本，其中以空格分隔为若干个单词，以'.'结束。你要输出这行文本中每个单词的长度。这里的单词与语言无关，可以包括各种符号，比如“it's”算一个单词，长度为4。注意，行中可能出现连续的空格。

// 输入：It's great to see you here.
// 输出： 4 5 2 3 3 4 （最后的句号不计入单词长度）

#include <stdio.h>

int main() {
    int count = 0;
    char ltr;

    while (1) {
        scanf("%c", &ltr);
        if (ltr == '.') {
            printf("%d", count);
            break;
        }

        if (ltr == ' ') {
            printf("%d ", count);
            count = 0;
        } else {
            count++;
        }
    }

    return 0;
}