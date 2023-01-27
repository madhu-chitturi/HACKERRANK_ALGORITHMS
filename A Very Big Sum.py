#include<stdio.h>
int main()
{
    //int sum=0,i;
    long int a[1000],sum=0,i,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    scanf("%ld",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        sum=sum+a[i];
    }
    printf("%ld",sum);
    return 0;
}
