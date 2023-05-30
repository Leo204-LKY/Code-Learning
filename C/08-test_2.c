#include <stdio.h>
#include <string.h>
int main(void)
{
    char *a=(char*)malloc(1000*sizeof(char));
	// char a[1000];
    char end[]="END";
    int h,h1,h2,m1,m2,s1,s2;    //hhmmss以及需要UTC+8的小时数h
    // while(gets(a)!="END")    //这样比较的是地址
    do
    {
        scanf("%s",a);
        if(a[0]=='$'&&a[1]=='G'&&a[2]=='P'&&a[3]=='R'&&a[4]=='M'&&a[5]=='C')//$GPRMC,
        {
            int i;
            int t;
            i=0;
            t=0;
            while(a[i+1]!='*')                        //校验开始 
            {
                i++;
                t=a[i]^t;
            }
            t=t%65536;
            
            if(a[i+2]>='A'&&a[i+2]<='F') {
                t=t-(a[i+2]-'A'+10)*16;
            } else {
                t=t-(a[i+2]-'0')*16;
            }
            if(a[i+3]>='A'&&a[i+2]<='F')
            {
                t=t-(a[i+3]-'A'+10);
            } else {
                t=t-(a[i+3]-'0');
            }                                            
            if(t==0)                                        //校验 
            {
                h1=a[7]-'0';
                h2=a[8]-'0';
                m1=a[9]-'0';
                m2=a[10]-'0';
                s1=a[11]-'0';
                s2=a[12]-'0';
            }
        }
    }while(strcmp(a,end)!=0);//while(k>0);
    h=h1*10+h2;
    h=(h+8)%24;
    printf("%02d:%d%d:%d%d",h,m1,m2,s1,s2);
    return 0;
}
/*
解答来自：
https://blog.csdn.net/sayinginging/article/details/121299197
*/