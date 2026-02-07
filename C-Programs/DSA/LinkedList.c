#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void insertBeginning(struct Node** head, int value);
void insertEnd(struct Node** head, int value);
void insertAtPosition(struct Node** head, int value, int pos);
void deleteNode(struct Node** head, int value);
void display(struct Node* head);
void sortList(struct Node* head);
void reverseList(struct Node** head);
void reverseDisplay(struct Node* head);




int main() {
    struct Node* head = NULL;
    int choice, value, pos;

    while (1) {
        printf("\n--- Linked List Operations ---\n");
        printf("1. Insert at Beginning\n");
        printf("2. Insert at End\n");
        printf("3. Insert at Specific Position\n");
        printf("4. Delete Node\n");
        printf("5. Display List\n");
        printf("6. Sort List\n");
        printf("7. Reverse List\n");
        printf("8. Reverse Display\n");
        printf("9. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insertBeginning(&head, value);
                break;
            case 2:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insertEnd(&head, value);
                break;
            case 3:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                printf("Enter position: ");
                scanf("%d", &pos);
                insertAtPosition(&head, value, pos);
                break;
            case 4:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                deleteNode(&head, value);
                break;
            case 5:
                display(head);
                break;
            case 6:
                sortList(head);
                break;
            case 7:
                reverseList(&head);
                break;
            case 8:
                printf("Reversed List: ");
                reverseDisplay(head);
                printf("\n");
                break;
            case 9:
                exit(0);
            default:
                printf("Invalid choice! Try again.\n");
        }
    }

    return 0;
}
