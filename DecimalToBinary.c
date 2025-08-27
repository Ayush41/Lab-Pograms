#include<stdio.h>

int main(){
    // printf("Program has been initialized...\n");
    printf("Program to convert Decimal to binary\n");
    
    int r=0,num;
    int i=0;
    //taking input
    printf("\nEnter the number in decimal:-\n");
    scanf("%d",&num);
    printf("\n\n\t\t\t\t");

   while(num>0){
        r = num%2;
        num=num/2;
        printf("   \b\b%d",r);
        // Sleep(1000);
    }
    return 0;
}