#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node* next;
};
struct Stack {
    struct Node* top;
};

int main(){

    printf("Stack using Linked List\n");
    do{
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        int choice;
        scanf("%d", &choice);

        switch(choice){
            case 1:
                // Code for push operation
                break;
            case 2:
                // Code for pop operation
                break;
            case 3:
                // Code for display operation
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice! Try again.\n");
        }
    }while(1);

    return 0;
}