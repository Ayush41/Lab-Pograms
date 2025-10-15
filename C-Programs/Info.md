# C Programming Solutions

This document contains solutions for various C programming problems.

## Q1. Program in C to Calculate Factorial of Each Element of the Array

### **Problem Description:**
Write a program in C to calculate the factorial of each element in an array.

### **Solution:**

```c
#include <stdio.h>

int main() {
    // Calculate the factorial of each element of the array
    int n;
    printf("Enter the num of elements in array:");
    scanf("%d", &n);

    int arr[n];

    // Input array elements
    printf("Enter elements of array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Factorials of the elements in the array:\n");
    for (int i = 0; i < n; i++) {
        int fact = 1;

        // Calculate factorial of arr[i]
        for (int j = 1; j <= arr[i]; j++) {
            fact *= j;
        }

        // Display the factorial of the current element
        printf("Factorial of %d = %d\n", arr[i], fact);
    }

    return 0;
}
```

## Q2. Q2. Program in C to modify array elements in such a way that the prestored elements should be replaced with the factorial of that number.

### **Problem Description:**
Write a program in C to modify array elements in such a way that the prestored elements should be replaced with the factorial of that number.

### **Solution:**

```c
#include<stdio.h>

int main() {
    int n;

    // Input
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    int arr[n];

    // Input elements
    printf("Enter elements of the array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Replace elements with itz factorail
    for (int i = 0; i < n; i++) {
        int fact=1;

        // Calculate factorial of arr[i]
        for (int j = 1; j <= arr[i]; j++) {
            fact *= j;
        }

        // Replace the element with its factorial
        arr[i] = fact;
    }

    // Display the modified array
    printf("Modified array (elements replaced with their factorials):\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}

```