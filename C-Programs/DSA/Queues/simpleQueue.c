#include<stdio.h>
#include<stdlib.h>

// what is queues 
// A queue is a linear data structure that follows the FIFO (First In First Out) principle.
// Elements are added at the rear and removed from the front.

// Operations in simple queues are ->
// 1. Enqueue (add element)
int EnQ(int front,int rear, int size, int queue[], int value){
    if(rear == size - 1){
        printf("Queue is full\n");
        return -1;
    }
    rear++;
    queue[rear] = value;
    return rear;
}

// 2. Dequeue (remove element)
int DeQ(){

}
// 3. Front (view front element)
// 4. Rear (view rear element)
// 5. isEmpty (check if queue is empty)
int isEmpty(){

}
// 6. isFull (check if queue is full)
int isFull(){

}



int main(){


}