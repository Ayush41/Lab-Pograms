# Function and Recursion programs
1. Program to Function to calculate the power of a number without 
using pow inbuilt function
```c []
#include <stdio.h>

// Function to calculate power without using pow()
int power(int base, int exp) {
    int result = 1;
    int current = base;

    while (exp > 0) {
        if (exp % 2 == 1) {        // If exponent is odd
            result *= current;
        }
        current *= current;        // Square the base
        exp /= 2;                  // Divide exponent by 2
    }

    return result;
}

int main() {
    int base, exp;

    printf("Enter base value: ");
    scanf("%d", &base);

    printf("Enter exponent/power value: ");
    scanf("%d", &exp);

    int result = power(base, exp);  // ✅ Store the returned value
    printf("%d raised to the power %d = %d\n", base, exp, result);

    return 0;
}

```

2. Program using functions to find hcf of two numbers

3. function to generate the fibonacci series using recursion
4. recursive fnction to find factorial of a number
```c []
#include<stdio.h>

int factorial(int n){
    if(n==0 || n==1)
        return 1;
    else
        return n*factorial(n-1);

}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num < 0)
        printf("Factorial of a negative number doesn't exist.\n");
    else
        printf("Factorial of %d = %d\n", num, factorial(num));
    return 0;
}

```
5. write a menu driven program using function for calculator operations. +,-,*,/
