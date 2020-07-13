#include<stdio.h>
int main()
{

    int n;
    scanf("%d",&n);
    int total_len = n;
    if (n>9){
        int temp = n-9;

        total_len = 9+(temp*2);

    }
    total_len = total_len+n;
   // printf("%d\n",total_len);
    int i ,j,z,h;
    int num = 97;
    for( i=0;i<n;i++)
    {
        for( j=0;j<i+1;j++)
        {

            printf("%d",j+1);

        }
        if ((j+1)>10){
            total_len-=1;
        }
        for(z=0;z<total_len-(2*j);z++)
        {

            printf(" ");

        }
        for(h=0;h<i+1;h++){
            printf("%c",num-h);

        }
        num++;
        printf("\n");

    }


}
