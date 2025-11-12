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
```c []
#include <stdio.h>

// Function to calculate HCF of two numbers
int hcf(int a, int b) {
    int min, i, hcf = 1;

    // Find the smaller number
    min = (a < b) ? a : b;

    // Loop from 1 to min to find HCF
    for(i = 1; i <= min; i++) {
        if(a % i == 0 && b % i == 0) {
            hcf = i;
        }
    }
    return hcf;
}
int main() {
    int num1, num2;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);
    int result = hcf(num1, num2);
    printf("HCF of %d and %d is %d\n", num1, num2, result);

    return 0;
}

3. function to generate the fibonacci series using recursion
```c []
#include<stdio.h>
//eg 1,1,2,3,5,8
int fibonacci(int n){
        if (n == 0)
        return 0;       // Base case 1
    else if (n == 1)
        return 1;       // Base case 2
    else
        return fibonacci(n - 1) + fibonacci(n - 2); // Recursive call
}

int main(){
    int n,i;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: ");
    for (i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }

    printf("\n");
    return 0;
}
```
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
```c []
#include <stdio.h>

// Function prototypes
float add(float a, float b);
float subtract(float a, float b);
float multiply(float a, float b);
float divide(float a, float b);

int main() {
    int choice;
    float num1, num2, result;

    do {
        // Display menu
        printf("\n--- Calculator Menu ---\n");
        printf("1. Addition (+)\n");
        printf("2. Subtraction (-)\n");
        printf("3. Multiplication (*)\n");
        printf("4. Division (/)\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if(choice >= 1 && choice <= 4) {
            printf("Enter two numbers: ");
            scanf("%f %f", &num1, &num2);
        }

        switch(choice) {
            case 1:
                result = add(num1, num2);
                printf("Result: %.2f\n", result);
                break;
            case 2:
                result = subtract(num1, num2);
                printf("Result: %.2f\n", result);
                break;
            case 3:
                result = multiply(num1, num2);
                printf("Result: %.2f\n", result);
                break;
            case 4:
                if(num2 != 0) {
                    result = divide(num1, num2);
                    printf("Result: %.2f\n", result);
                } else {
                    printf("Error: Division by zero is not allowed.\n");
                }
                break;
            case 5:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }

    } while(choice != 5);

    return 0;
}

// Function definitions
float add(float a, float b) {
    return a + b;
}

float subtract(float a, float b) {
    return a - b;
}

float multiply(float a, float b) {
    return a * b;
}

float divide(float a, float b) {
    return a / b;
}
```