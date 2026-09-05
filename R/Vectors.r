print("I am Iron Man")

str1 <- "This is an String"
print (str1)


# Vector arithmetic & Logical operations on vector 

# Taking user input

# Creating a Vector V1 & V2 
v1 <- c(10,20,30,40,50,60,70)
v2 <- c(11,22,33,44,55,66,77)

# Indexing and Subsetting
v1[1] # 10
v2[4] # 44


print(v1[c(1, 3, 5)])

v1[1:3]

v1[v1>5]

# Demonstrate mixing of different type of obj and conversion between data types.


# Logical Operations 
print(v1 > v2)
print(v1 < v2)
print(v1 == v2)
print(v1 != v2)
print(v1 >= v2)
print(v1 <= v2)

print(v1 > 30 & v2 > 30) # Logical AND

print(v1 > 60 | v2 > 60) # Logical OR | 

# arithmetic operations

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print(v1 %% v2)
print(v1 ^ v2) 