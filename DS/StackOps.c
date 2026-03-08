#include<stdio.h>
#define MAX 5
// Stack implemetation
int push(int stack[],int top);
int pop(int stack[],int top);
void peek(int stack[],int top);
void display(int stack[], int top);

int push(int stack[], int top){
    int x;
    if(top==MAX-1){
        printf("Stack overflow");
    }else{
        printf("Enter value to push:");
        scanf("%d",&x);
        top++;
        stack[top]=x;
    return top;
    }
}
int pop(int stack[], int top){
    if(top==1){
        printf("Stack Underflow");
    }
    else{
        printf("Popped element");
        top--;
    return top;
    }
}
void peek(int stack[],int top){
    // the value on top of stack
    if(top==-1){
        printf("Stack is empty");
    }
    else{
        printf("Top Element: %d",stack[top]);
    }
}

void display(int stack[],int top){
    if(top==-1){
        printf("Stack is Empty");
    }else{
        printf("Stack elements:\n");
        while(top>=0){
            printf(" %d ",stack[top]);
            top--;
        }
    }
}

int main(){
    
    int stack[MAX], top =-1;
    int ch;
    
    do{
        printf("--\n\n\tMenu of Stack Ops\n\n--");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        
        printf("Enter choice:");
        scanf("%d",&ch);
        
        switch(ch){
            case 1: 
            top = push(stack,top);
            break;
            
            case 2:
            top = pop(stack,top); 
            break;
            
            case 3:
            peek(stack,top);
            break;
            
            case 4:
            display(stack,top);
            break;
            
            case 5:
            printf("Exit\n");
            break;
            
            default:
            printf("Invalid choice");
        }
        
        
    }while(ch!=5);
    
    return 0;
}