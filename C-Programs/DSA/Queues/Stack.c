// Stack Implementation with All Operations
// LIFO - Last In First Out Data Structure
#include<stdio.h>
#include<stdlib.h>

#define MAX 100

// Stack structure
typedef struct {
    int arr[MAX];
    int top;
} Stack;

// Initialize stack
void initStack(Stack *s) {
    s->top = -1;
    printf("Stack initialized successfully!\n");
}

// Check if stack is empty
int isEmpty(Stack *s) {
    return (s->top == -1);
}

// Check if stack is full
int isFull(Stack *s) {
    return (s->top == MAX - 1);
}

// Push operation: Add element to top of stack
void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack Overflow! Cannot push %d. Stack is full.\n", value);
        return;
    }
    s->arr[++s->top] = value;
    printf("Pushed: %d\n", value);
}

// Pop operation: Remove and return element from top of stack
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow! Cannot pop. Stack is empty.\n");
        return -1;
    }
    int value = s->arr[s->top--];
    printf("Popped: %d\n", value);
    return value;
}

// Peek operation: View top element without removing it
int peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty! No element to peek.\n");
        return -1;
    }
    return s->arr[s->top];
}

// Count operation: Return number of elements in stack
int count(Stack *s) {
    return (s->top + 1);
}

// Display all elements in stack
void display(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return;
    }

    printf("Stack elements (Top to Bottom): ");
    for (int i = s->top; i >= 0; i--) {
        printf("%d ", s->arr[i]);
    }
    printf("\n");
}

// Display detailed stack information
void displayStackInfo(Stack *s) {
    printf("\n========== STACK INFORMATION ==========\n");
    printf("Stack Size: %d\n", MAX);
    printf("Current Elements: %d\n", count(s));
    printf("Available Space: %d\n", MAX - count(s));
    printf("Is Empty: %s\n", isEmpty(s) ? "YES" : "NO");
    printf("Is Full: %s\n", isFull(s) ? "YES" : "NO");
    printf("Top Position: %d\n", s->top);
    if (!isEmpty(s)) {
        printf("Top Element: %d\n", peek(s));
    }
    printf("========================================\n\n");
}

// Clear the stack
void clearStack(Stack *s) {
    s->top = -1;
    printf("Stack cleared successfully!\n");
}

// Search for an element in stack (returns position from top, or -1 if not found)
int search(Stack *s, int value) {
    for (int i = s->top; i >= 0; i--) {
        if (s->arr[i] == value) {
            return (s->top - i);  // Position from top
        }
    }
    return -1;
}

// Display menu
void displayMenu() {
    printf("\n========== STACK OPERATIONS MENU ==========\n");
    printf("1. Push (Add element)\n");
    printf("2. Pop (Remove element)\n");
    printf("3. Peek (View top element)\n");
    printf("4. Display Stack\n");
    printf("5. Check if Stack is Empty\n");
    printf("6. Check if Stack is Full\n");
    printf("7. Count Elements\n");
    printf("8. Search Element\n");
    printf("9. Clear Stack\n");
    printf("10. Stack Information\n");
    printf("11. Exit\n");
    printf("============================================\n");
    printf("Enter your choice: ");
}

int main() {
    Stack s;
    initStack(&s);

    int choice, value, result;

    printf("╔════════════════════════════════════════╗\n");
    printf("║   STACK IMPLEMENTATION (LIFO)          ║\n");
    printf("║   Last In First Out Data Structure    ║\n");
    printf("╚════════════════════════════════════════╝\n\n");

    while (1) {
        displayMenu();
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                // Push operation
                printf("Enter the value to push: ");
                scanf("%d", &value);
                push(&s, value);
                break;
            }

            case 2: {
                // Pop operation
                result = pop(&s);
                if (result != -1) {
                    printf("Returned value: %d\n", result);
                }
                break;
            }

            case 3: {
                // Peek operation
                result = peek(&s);
                if (result != -1) {
                    printf("Top element: %d\n", result);
                }
                break;
            }

            case 4: {
                // Display stack
                display(&s);
                break;
            }

            case 5: {
                // Check if empty
                if (isEmpty(&s)) {
                    printf("Stack is EMPTY!\n");
                } else {
                    printf("Stack is NOT empty!\n");
                }
                break;
            }

            case 6: {
                // Check if full
                if (isFull(&s)) {
                    printf("Stack is FULL!\n");
                } else {
                    printf("Stack is NOT full! Available space: %d\n", MAX - count(&s));
                }
                break;
            }

            case 7: {
                // Count elements
                printf("Total elements in stack: %d\n", count(&s));
                break;
            }

            case 8: {
                // Search element
                printf("Enter the value to search: ");
                scanf("%d", &value);
                result = search(&s, value);
                if (result != -1) {
                    printf("Element found at position %d from top\n", result);
                } else {
                    printf("Element not found in stack!\n");
                }
                break;
            }

            case 9: {
                // Clear stack
                clearStack(&s);
                break;
            }

            case 10: {
                // Display stack information
                displayStackInfo(&s);
                break;
            }

            case 11: {
                // Exit
                printf("\nThank you for using Stack implementation! Exiting...\n");
                return 0;
            }

            default: {
                printf("Invalid choice! Please select a valid option (1-11).\n");
            }
        }
    }

    return 0;
}
