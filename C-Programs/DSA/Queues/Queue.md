# Queue Data Structure - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Characteristics](#characteristics)
3. [Operations](#operations)
4. [Time Complexity](#time-complexity)
5. [Space Complexity](#space-complexity)
6. [Implementation](#implementation)
7. [Types of Queues](#types-of-queues)
8. [Advantages and Disadvantages](#advantages-and-disadvantages)
9. [Real-World Applications](#real-world-applications)

---

## Introduction

### What is a Queue?

A **Queue** is a linear data structure that follows the **FIFO (First In First Out)** principle. This means that the element inserted first into the queue will be the first one to be removed from the queue.

Think of a real-world example: a queue at a movie ticket counter where the person who arrives first gets the ticket first.

### Key Concept

```
Enqueue (Add) at REAR → [Element1, Element2, Element3] ← Dequeue (Remove) from FRONT
```

---

## Characteristics

| Property | Description |
|----------|-------------|
| **Order** | FIFO - First In First Out |
| **Insertion** | Elements are added at the **rear** (end) |
| **Deletion** | Elements are removed from the **front** (beginning) |
| **Linear** | Elements are arranged in a linear sequence |
| **Dynamic** | Can be static (array) or dynamic (linked list) |

---

## Operations

### 1. **Enqueue** (Insert/Add Element)
- Adds an element to the rear of the queue
- Precondition: Queue must not be full
- Time Complexity: O(1)

```
Before: [1, 2, 3, _, _]
After Enqueue(4): [1, 2, 3, 4, _]
                       ↑
                      rear
```

### 2. **Dequeue** (Remove Element)
- Removes and returns the element from the front
- Precondition: Queue must not be empty
- Time Complexity: O(1)

```
Before: [1, 2, 3, 4, _]
After Dequeue(): [_, 2, 3, 4, _]
        ↑
       front
```

### 3. **Front** (Peek Front)
- Returns the front element without removing it
- Time Complexity: O(1)
- Does not modify the queue

### 4. **Rear** (Peek Rear)
- Returns the rear element without removing it
- Time Complexity: O(1)
- Does not modify the queue

### 5. **isEmpty**
- Checks if the queue is empty
- Returns: `true` if empty, `false` otherwise
- Time Complexity: O(1)

### 6. **isFull**
- Checks if the queue is full (only for static arrays)
- Returns: `true` if full, `false` otherwise
- Time Complexity: O(1)

---

## Time Complexity

| Operation | Array Implementation | Linked List Implementation |
|-----------|----------------------|-----------------------------|
| Enqueue | O(1) | O(1) |
| Dequeue | O(n) * | O(1) |
| Front | O(1) | O(1) |
| Rear | O(1) | O(1) |
| isEmpty | O(1) | O(1) |
| isFull | O(1) | N/A |

*In simple array implementation, dequeue requires shifting elements (O(n)). Use circular queue to achieve O(1).

---

## Space Complexity

| Implementation | Space Complexity |
|---|---|
| Simple Array Queue | O(n) |
| Circular Queue | O(n) |
| Linked List Queue | O(n) |

Where `n` is the number of elements in the queue.

---

## Implementation

### Simple Queue using Array

```c
#include<stdio.h>
#include<stdlib.h>

#define MAX 100

typedef struct {
    int front;
    int rear;
    int queue[MAX];
} Queue;

// Initialize queue
void initQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

// Check if queue is empty
int isEmpty(Queue *q) {
    return (q->front == -1 || q->front > q->rear);
}

// Check if queue is full
int isFull(Queue *q) {
    return (q->rear == MAX - 1);
}

// Enqueue operation
int enqueue(Queue *q, int value) {
    if (isFull(q)) {
        printf("Queue is full! Cannot enqueue.\n");
        return 0;
    }
    if (q->front == -1) {
        q->front = 0;
    }
    q->queue[++q->rear] = value;
    printf("Enqueued: %d\n", value);
    return 1;
}

// Dequeue operation
int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty! Cannot dequeue.\n");
        return -1;
    }
    int value = q->queue[q->front++];
    printf("Dequeued: %d\n", value);
    return value;
}

// Display queue
void display(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty!\n");
        return;
    }
    printf("Queue elements: ");
    for (int i = q->front; i <= q->rear; i++) {
        printf("%d ", q->queue[i]);
    }
    printf("\n");
}
```

---

## Types of Queues

### 1. **Simple Queue (Linear Queue)**
- Basic implementation using array
- **Disadvantage**: Space wastage due to shifting (dequeue operation)
- Suitable for small applications

### 2. **Circular Queue**
- Rear pointer wraps around to front when it reaches the end
- **Advantage**: Efficient use of array space
- **Disadvantage**: Slightly more complex implementation
- Used in CPU scheduling, memory management

### 3. **Priority Queue**
- Elements are processed based on priority, not FIFO order
- Higher priority elements are dequeued first
- Used in: Operating systems, Dijkstra's algorithm

### 4. **Double-Ended Queue (Deque)**
- Allows insertion and deletion from both ends
- Combines features of queue and stack
- Used in: Sliding window problems, scheduling

### 5. **Queue using Linked List**
- Dynamic memory allocation
- **Advantage**: No space wastage, no fixed size limit
- **Disadvantage**: Extra memory for pointers
- Better for large datasets

---

## Advantages and Disadvantages

### ✅ Advantages

1. **Efficient Operation**: Constant time O(1) for enqueue and dequeue (with proper implementation)
2. **Fair Processing**: FIFO principle ensures fairness
3. **Easy to Implement**: Simple and straightforward
4. **Real-world Relevance**: Models many real-world situations
5. **Memory Efficient**: When implemented using circular queue or linked list

### ❌ Disadvantages

1. **Space Wastage**: In simple array queue, space is wasted after dequeue operations
2. **Fixed Size**: Array-based queues have a fixed maximum size
3. **One-directional**: Can only add at rear and remove from front
4. **Less Flexible**: Compared to other data structures for specific use cases

---

## Real-World Applications

### 1. **Operating Systems**
- **CPU Scheduling**: Process scheduling (Round Robin)
- **Disk I/O Scheduling**: Managing disk requests
- **Memory Management**: Page replacement algorithms

### 2. **Networking**
- **Packet Queuing**: Routers and network devices
- **Message Queuing**: In distributed systems
- **Bandwidth Management**: Traffic shaping

### 3. **Customer Service**
- **Customer Service Centers**: Help desk ticket management
- **Hospital Triage**: Patient queue management
- **ATM Queues**: Banking transactions

### 4. **Simulation and Games**
- **Event Scheduling**: Game event processing
- **Breadth-First Search (BFS)**: Graph traversal
- **Level-order Tree Traversal**: Binary tree operations

### 5. **Printers and Resources**
- **Print Queue**: Managing print jobs
- **Resource Allocation**: Distributing shared resources

### 6. **Data Streaming**
- **Video Buffering**: Streaming applications
- **Keyboard Input Buffer**: Character buffering
- **Data Pipeline**: ETL (Extract, Transform, Load) processes

### 7. **Real-time Systems**
- **Robotics**: Task scheduling
- **Real-time Notifications**: Event-driven systems
- **Traffic Management**: Vehicle routing

---

## Comparison with Other Data Structures

| Feature | Queue | Stack | Array | Linked List |
|---------|-------|-------|-------|-------------|
| Order | FIFO | LIFO | Random Access | Sequential |
| Insertion | Rear | Top | Any Position | Sequential |
| Deletion | Front | Top | Any Position | Sequential |
| Time - Enqueue/Push | O(1) | O(1) | O(1) | O(1) |
| Time - Dequeue/Pop | O(1)* | O(1) | O(n) | O(1) |
| Space | O(n) | O(n) | O(n) | O(n) |

---

## Summary

- **Queue** is essential for implementing fair resource management
- **FIFO principle** ensures sequential processing
- **Various implementations** suit different requirements
- **Applications** range from OS to real-world scenarios
- **Choose implementation** based on specific use case needs



Q1.write a program to implement all the operations of queue using 2 stacks. FIFO.