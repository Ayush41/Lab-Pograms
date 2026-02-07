// Q1.write a program to implement all the operations of queue using 2 stacks.
#include<stdio.h>
#include<stdlib.h>

#define MAX 100

// Stack structure
typedef struct {
    int arr[MAX];
    int top;
} Stack;

// Queue using 2 stacks
typedef struct {
    Stack stack1;  // Stack 1: Used for push operations (enqueue)
    Stack stack2;  // Stack 2: Used for pop operations (dequeue)
} QueueUsing2Stacks;

// Initialize a stack
void initStack(Stack *s) {
    s->top = -1;
}

// Check if stack is empty
int isStackEmpty(Stack *s) {
    return (s->top == -1);
}

// Check if stack is full
int isStackFull(Stack *s) {
    return (s->top == MAX - 1);
}

// Push element to stack
void push(Stack *s, int value) {
    if (isStackFull(s)) {
        printf("Stack Overflow!\n");
        return;
    }
    s->arr[++s->top] = value;
}

// Pop element from stack
int pop(Stack *s) {
    if (isStackEmpty(s)) {
        return -1;
    }
    return s->arr[s->top--];
}

// Peek top element of stack
int peek(Stack *s) {
    if (isStackEmpty(s)) {
        return -1;
    }
    return s->arr[s->top];
}

// Initialize Queue using 2 stacks
void initQueue(QueueUsing2Stacks *q) {
    initStack(&q->stack1);
    initStack(&q->stack2);
}

// Check if queue is empty
int isQueueEmpty(QueueUsing2Stacks *q) {
    return (isStackEmpty(&q->stack1) && isStackEmpty(&q->stack2));
}

// Enqueue operation: Push element to stack1
void enqueue(QueueUsing2Stacks *q, int value) {
    push(&q->stack1, value);
    printf("Enqueued: %d\n", value);
}

// Dequeue operation: Pop from stack2, if empty, move all elements from stack1 to stack2
int dequeue(QueueUsing2Stacks *q) {
    // If both stacks are empty, queue is empty
    if (isStackEmpty(&q->stack2) && isStackEmpty(&q->stack1)) {
        printf("Queue is empty! Cannot dequeue.\n");
        return -1;
    }

    // If stack2 is empty, transfer all elements from stack1 to stack2
    // This reverses the order, making the oldest element (first enqueued) on top of stack2
    if (isStackEmpty(&q->stack2)) {
        while (!isStackEmpty(&q->stack1)) {
            push(&q->stack2, pop(&q->stack1));
        }
    }

    // Pop from stack2
    int value = pop(&q->stack2);
    printf("Dequeued: %d\n", value);
    return value;
}

// Peek at front element of queue
int peekFront(QueueUsing2Stacks *q) {
    // If stack2 has elements, front is at top of stack2
    if (!isStackEmpty(&q->stack2)) {
        return peek(&q->stack2);
    }

    // If stack2 is empty, transfer from stack1 and peek
    if (!isStackEmpty(&q->stack1)) {
        while (!isStackEmpty(&q->stack1)) {
            push(&q->stack2, pop(&q->stack1));
        }
        return peek(&q->stack2);
    }

    printf("Queue is empty!\n");
    return -1;
}

// Display queue (simulating all elements from front to rear)
void displayQueue(QueueUsing2Stacks *q) {
    if (isQueueEmpty(q)) {
        printf("Queue is empty!\n");
        return;
    }

    printf("Queue elements (Front to Rear): ");

    // Create temporary stack to display without modifying queue
    Stack temp;
    initStack(&temp);

    // If stack2 has elements, display them first (they are in correct order)
    if (!isStackEmpty(&q->stack2)) {
        // Copy stack2 to temp to display in correct order
        for (int i = 0; i <= q->stack2.top; i++) {
            printf("%d ", q->stack2.arr[i]);
        }
    }

    // Display elements from stack1 in reverse order
    if (!isStackEmpty(&q->stack1)) {
        for (int i = q->stack1.top; i >= 0; i--) {
            printf("%d ", q->stack1.arr[i]);
        }
    }

    printf("\n");
}

// Detailed menu-driven program
void displayMenu() {
    printf("\n========== QUEUE USING 2 STACKS ==========\n");
    printf("1. Enqueue (Add element)\n");
    printf("2. Dequeue (Remove element)\n");
    printf("3. Peek Front element\n");
    printf("4. Display Queue\n");
    printf("5. Check if Queue is Empty\n");
    printf("6. Exit\n");
    printf("==========================================\n");
    printf("Enter your choice: ");
}

int main() {
    QueueUsing2Stacks q;
    initQueue(&q);

    int choice, value;

    printf("*** QUEUE IMPLEMENTATION USING 2 STACKS ***\n");
    printf("This program demonstrates FIFO (First In First Out) behavior using 2 stacks.\n\n");

    while (1) {
        displayMenu();
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the value to enqueue: ");
                scanf("%d", &value);
                enqueue(&q, value);
                break;

            case 2:
                dequeue(&q);
                break;

            case 3: {
                int frontVal = peekFront(&q);
                if (frontVal != -1) {
                    printf("Front element: %d\n", frontVal);
                }
                break;
            }

            case 4:
                displayQueue(&q);
                break;

            case 5:
                if (isQueueEmpty(&q)) {
                    printf("Queue is EMPTY!\n");
                } else {
                    printf("Queue is NOT empty!\n");
                }
                break;

            case 6:
                printf("Exiting program. Thank you!\n");
                return 0;

            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}