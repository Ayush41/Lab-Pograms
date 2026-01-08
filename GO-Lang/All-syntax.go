package main

import ("fmt" "math")

func add(a,b int)int{
	return a+b 
}

func factorial(n int)int{
	if n ==0{
		return 1
	}
	return n*factorial(n-1)

}

func main(){
	var intVar int = 20
	intvar2 :=30

	fmt.Println("Sum of integers:", add(intvar2,intVar))
	fmt.Println("Factorial of 5:", factorial(5))
}
