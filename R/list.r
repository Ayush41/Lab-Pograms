# Q1. Create a list and manipulate list, strings, and factors in R

student_list <- list(
    Name = "Ayush Raj",
    Age = 20,
    Marks = c(85, 90, 78)
)

print(student_list)

# Access Name from the list
print(student_list$Name)

# Create a string
text <- "R Programming Language"

print(text)

# Create a factor
department <- factor(
    c("CSE", "IT", "ECE")
)

print(department)

# Display frequency of departments
print(table(department))


# Q2. Perform string operations and factor manipulation

text <- "R Programming Language"

# Convert string to uppercase
print(toupper(text))

# Convert string to lowercase
print(tolower(text))

# Find length of string
print(nchar(text))

# Replace text
new_text <- gsub("R", "Python", text)

print(new_text)

# Create a factor
department <- factor(
    c("CSE", "CSE", "IT", "ECE", "IT")
)

print(department)

# Display factor levels
print(levels(department))

# Display frequency of each department
print(table(department))


# Q3. Create and manipulate dataFrames using R

students <- data.frame(
    Name = c("Ayush", "Rahul", "Priya", "Amit"),
    Age = c(20, 21, 19, 22),
    Marks = c(85, 78, 92, 88),
    Department = c("CSE", "IT", "CSE", "ECE")
)

# Display data frame
print(students)

# Display first row
print(students[1, ])

# Display Name column
print(students$Name)

# Display Marks column
print(students$Marks)

# Add a new column
students$Grade <- c("A", "B", "A+", "A")

print(students)

# Find students with marks above 80
result <- students[students$Marks > 80, ]

print(result)

# Find average marks
average <- mean(students$Marks)

print(average)

# Sort students by marks
sorted_students <- students[order(students$Marks, decreasing = TRUE), ]

print(sorted_students)
