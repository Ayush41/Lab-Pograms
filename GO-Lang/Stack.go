package main

import (
	"fmt"
)

type Stack struct {
	items []interface{}
}

// Push adds an element to the top of the stack
func (s *Stack) Push(item interface{}) {

}

// Pop removes and returns the top element from the stack
func (s *Stack) Pop() (interface{}, error) {

}

// Peek returns the top element without removing it
func (s *Stack) Peek() (interface{}, error) {

}

// IsEmpty checks if the stack is empty
func (s *Stack) IsEmpty() bool {

}

// Size returns the number of elements in the stack
func (s *Stack) Size() int {

}

// Clear removes all elements from the stack
func (s *Stack) Clear() {

}

func main() {
	stack := &Stack{}
}