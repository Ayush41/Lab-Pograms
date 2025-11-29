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
### Q6.
SELECT emp_name
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE location = 'New York'
);
