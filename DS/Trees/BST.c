#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    int data;
    struct Node* left;
    struct Node* right;
}node;

void insert(node** root,int data){

}
void preorder(node* root){

}
void inorder(node* root){
    
}
void postorder(node* root){
    
}
node* search(node* root,int data){
    return NULL;
}
void delete(node** root,int data){
    
}


int main(){

    // Creating a new node
    node* root = (node*)malloc(sizeof(node));
    root->data = 10;
    root->left = NULL;
    root->right = NULL;

    // creating menu driven program for BST -> Insert, Preorder,inorder,postorder, search, delete,exit
    // Implementation for each operation will go here
    char choice;
    do{
        printf("Enter your choice: \n");
        printf("1. Insert\n");
        printf("2. Preorder\n");
        printf("3. Inorder\n");
        printf("4. Postorder\n");
        printf("5. Search\n");
        printf("6. Delete\n");
        printf("7. Exit\n");
        scanf("%c", &choice);

        switch(choice){
            case '1':
                // Insert operation
                break;
            case '2':
                // Preorder operation
                break;
            case '3':
                // Inorder operation
                break;
            case '4':
                // Postorder operation
                break;
            case '5':
                // Search operation
                break;
            case '6':
                // Delete operation
                break;
            case '7':
                // Exit operation
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while(choice != '7');


    return 0;

}