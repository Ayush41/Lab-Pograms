#include<stdio.h>

int main(){
    int num;
    printf("\nEnter num to check Odd/Even:-");
    scanf("%d",&num);

    if(num & 1){
        printf("is ODD");
    }else{
        printf("Is Even");
    }

    return 0;
}