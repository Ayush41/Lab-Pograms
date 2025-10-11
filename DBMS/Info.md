# DBMS Labs - Oracle Database Queries

This repository contains all the DBMS queries and lab exercises I have worked on during my Database Management Systems (DBMS) course, specifically using Oracle Database.

The repository includes the following:

- SQL queries for various DBMS concepts and topics.
- Solutions for lab exercises and assignments.
- Scripts for creating and managing database objects like tables, views, and indexes in Oracle DB.


## Prerequisites

- Oracle Database (or any compatible version)
- SQL*Plus or Oracle SQL Developer for executing the queries


## 📊 Aggregate Functions in Oracle SQL

**Aggregate functions** perform a calculation on a set of values and return a single value. They are commonly used with the `GROUP BY` clause.

Here are the commonly used aggregate functions in Oracle SQL:

| Function | Description |
|----------|-------------|
| `AVG()`  | Returns the average value of a numeric column |
| `COUNT()` | Returns the number of rows (can count all rows or only non-null values) |
| `MAX()`  | Returns the maximum value from a column |
| `MIN()`  | Returns the minimum value from a column |
| `SUM()`  | Returns the total sum of a numeric column |


### 🧪 Example:

```sql
SELECT department_id, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;



## ❓ Questions and SQL Queries

### 1. Count the total number of employees

```sql
SELECT COUNT(*) AS total_count 
FROM employee;
```

### 2. Count employees earning more than 10,000
```sql
SELECT COUNT(*) AS totalEmp
FROM employees
WHERE salary > 10000;
```

```sql
SELECT department_id, COUNT(*) AS emp_count
FROM employees
WHERE salary > 10000
GROUP BY department_id;
```