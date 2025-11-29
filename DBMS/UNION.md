# 📘 SQL Lab – UNION, INTERSECT, MINUS & Subqueries

This document contains SQL table creation, sample data insertion, and solutions to lab questions involving **UNION**, **INTERSECT**, **MINUS**, and **subqueries**.

---

## 📌 0. Table Creation

```sql
CREATE TABLE departments (
    dept_id NUMBER PRIMARY KEY,
    dept_name VARCHAR2(30),
    location VARCHAR2(30)
);

CREATE TABLE employees (
    emp_id NUMBER PRIMARY KEY,
    emp_name VARCHAR2(30),
    salary NUMBER,
    dept_id NUMBER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

## INSERTING DATA TO BOTH TABLES

```sql
INSERT INTO departments VALUES (10, 'Finance', 'London');
INSERT INTO departments VALUES (20, 'Marketing', 'Chicago');
INSERT INTO departments VALUES (30, 'Sales', 'New York');
INSERT INTO departments VALUES (40, 'HR', 'London');
INSERT INTO departments VALUES (50, 'IT', 'Chicago');

INSERT INTO employees VALUES (1, 'John', 62000, 10);
INSERT INTO employees VALUES (2, 'Emma', 54000, 20);
INSERT INTO employees VALUES (3, 'Liam', 70000, 30);
INSERT INTO employees VALUES (4, 'Sophia', 58000, 40);
INSERT INTO employees VALUES (5, 'Ryan', 63000, 20);
INSERT INTO employees VALUES (6, 'Olivia', 50000, 50);

```

### 1. Display all departments and employees earning salary above 60000 together (no duplicates).
```sql
-- UNION file LabQUES1
SELECT dept_name AS result FROM departments
UNION
SELECT emp_name FROM employees
WHERE salary > 60000;
```

### 2. List employees who work in departments that exist in London OR Chicago only.
```sql
-- List employees who work in departments that exist in London OR Chicago only.
SELECT emp_name
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE location IN ('London', 'Chicago')
);
```
### 3. Names of employees whose salary is above 55000 OR departments that have 5–8 letters.
```sql
-- Names of employees whose salary is above 55000 OR departments that have 5–8 letters.
SELECT emp_name AS result
FROM employees
WHERE salary > 55000
UNION
SELECT dept_name
FROM departments
WHERE LENGTH(dept_name) BETWEEN 5 AND 8;
```

### 4. Provide the list of lowest salary employee + departments having minimum department_id.

```sql
-- Department with lowest salary
SELECT emp_name AS result
FROM employees
WHERE salary = (SELECT MIN(salary) FROM employees)
UNION
-- Department with smallest department_id:
SELECT dept_name
FROM departments
WHERE dept_id = (SELECT MIN(dept_id) FROM departments);
```

```sql
-- Q5. Emp whose salary matches ANY aggregated city based dept count

SELECT emp_name FROM EMPLOYEES
WHERE salary = ANY(
    SELECT COUNT(*) FROM DEPARTMENTS
    GROUP BY location
);
```
### Q6. Employees working in departments located in NY
SELECT emp_name
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE location = 'New York'
);

## ### 7. Departments whose IDs occur in both tables AND have employees earning above the overall average salary.

```sql
SELECT DISTINCT d.dept_id
FROM departments d
INTERSECT
SELECT dept_id
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### 8. 8. Departments located in cities where total employee salary per department is above 100000.

```sql
SELECT dept_name, location
FROM departments
WHERE dept_id IN (
    SELECT dept_id
    FROM employees
    GROUP BY dept_id
    HAVING SUM(salary) > 100000
);

```

### 9. Departments with IDs that match employees earning above average salary.

### 10. Employees earning above average salary MINUS employees in department 20.

### 11. Combine department names and employee names, but include duplicate department names based on employee count.

### 12. Show all employee salaries and department IDs (UNION). Remove all common numbers.

### 13. List all employee IDs except those belonging to department 10, and add all department IDs (including duplicates).