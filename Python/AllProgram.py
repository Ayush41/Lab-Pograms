# Program to find all palindrome number from 1 to N
try:
    n = int(input("Enter the limit(n):"))
    print(f"Palindrome num between 1 to {n} are:")
    
    for num in range(1,n+1):
        if str(num) == str(num)[::-1]:
            print(num,end=" ")
except ValueError:
    print("please enter a valid integer")



# Factorial using Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
num = int(input("Enter a number to find factorial: "))
fact = factorial(num)
print(f"The factorial of {num} is {fact}")

# Using Itertaion
def factorial_iter(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
num = int(input("Enter a number to find factorial using iteration: "))
fact = factorial_iter(num)
print(f"The factorial of {num} using iteration is {fact}")


# swap
a= 10
b = 20

# 1st way
a,b = b,a
print("single line swap is :",a,b)

# using temp 3rd var
temp = a
a = b
b = temp

print("swap using 3rd var temp:",a,b)

a = a^b
b = a^b
a=a^b
print("bitlevel swap is :",a,b)

a = a+b
b = a-b
a = a-b
print("arithmetic way to swap is :",a,b)



# Lambda Function
# program to square all num in list
mlist = [1,3,4,6,7,8,2]
print("Original List",mlist)

sqNum = list(map(lambda x:x**2, mlist))

print("squared list is:\n\n",sqNum)

# lambda arguemnts: expresssion
# Find value of (a+b)^2
formula = lambda a,b:(a+b)**2
x,y = 2,3
result = formula(x,y)
print(f"The result of ({x}+{y})^2 is: {result}")



# Custom Error
class NegNumError(Exception):
    pass
try:
    num = int(input("Enter a +ve num:"))
    if num<0:
        raise NegNumError("Negetive num not allowed")
    print(f"you entered {num}")
except NegNumError as e:
    print("Caugh Custom Error",e)
    
# EXception Handling
try: 
    num = int(input("Enter a num: "))
    result = 100/num
except ZeroDivisionError:
    print("Error! Cant divide by Zero!")
except ValueError:
    print("Error! Please enter a valid integer.")
else:
    print(f"The result is {result}")
finally:
    print("Execution Complete")

# # Short Circuit Evaluation
# a,b = 0,10

# if a!=0 and (b/a)>2:
#     print("This wont print")
# else:
#     print("Safe The div by zero was skipped")

# x = 5
# if x>0 or (b/0)==10:
#     print("this prints!, the rror on the right was ignored")


# True or False



#  Factorial
n= int(input("Enter Value :"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"factorial is {fact}")

# with while loop
fact =1
i=1
while i<=n:
    fact *= i
    i +=1
print(f"value of fact is {fact}")

# # Display all prime numbers between 1 to N
# try:
#     n= int(input("Enter Value of N prime numbers :"))
#     print(f"Prime numbers between 1 to {n}: ")
    
#     for num in range(2,n+1):
#         isPrime = True
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 isPrime = False
#                 break
#         if isPrime:
#             print(num, end=" ")
#     print()
# except ValueError:
#     print("Invlaid Input! enter a whole num")

# # Print program 1 to N
# n = int(input("Enter limit(n) :"))

# # with for loop
# for i in range(1,n+1):
#     print(i,end=" \n")
    
# # with while loop
# i=1
# while i<=n:
#     print(i,end= " \n")
#     # i=i+1
#     i +=1



# # Calculate salary 
# try:
#     total_sale = float(input("Enter total sale amount: "))
#     basic_sal = 4000
#     da = 1.10*basic_sal
#     conveyance = 500.0
    
#     if total_sale >= 100000:
#         hra = 0.20*basic_sal
#         incentive = 0.10*total_sale
#         bonus_type = "high permornce(col 1)"
#     else:
#         hra = 0.10*basic_sal
#         incentive =0.05*total_sale
#         bonus_type = "Standard performance(col 2)"
    
#     # Calculate gross salary
#     grossSal  = basic_sal +hra+da+conveyance+incentive
#     print("\n" + "="*30)
#     print("      SALARY SLIP")
#     print("="*30)
#     print(f"Applied Scheme   : {bonus_type}")
#     print(f"Basic Salary     : Rs {basic_sal:.2f}")
#     print(f"HRA              : Rs {hra:.2f}")
#     print(f"DA (110%)        : Rs {da:.2f}")
#     print(f"Conveyance       : Rs {conveyance:.2f}")
#     print(f"Incentive        : Rs {incentive:.2f}")
#     print("-" * 30)
#     print(f"TOTAL SALARY     : Rs {grossSal:.2f}")
#     print("="*30)
    
# except ValueError:
#     print("Invalid input! enter numeric val for sale")
    