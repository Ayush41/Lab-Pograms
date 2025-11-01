# SubQueries in Oracle SQL
The query nested inside another query is called subquery.

A subquery is a query inside another query.
It allows you to use the result of one SELECT statement as input for another.

## Syntax:
```sql
SELECT column_name
FROM table_name
WHERE column_name expression operator 
   (SELECT column_name FROM table_name WHERE ...);
```

### There are 4 types of subquery :
1. Single row subquery
2. Multiple row subquery
3. Nested row subquery
4. Corelated subquery

1. Single row subquery:
    - It returns only one row or value. 
    - It uses operators like =,<,>.

### Example Ques:
```sql
-- find an emp name whoose salary is greater than avg salary
SELECT firstname,lastname,salary 
FROM employees
WHERE salary > (
    SELECT AVG(salary) FROM employees
);

SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
-- or 
WHERE salary > avg(salary);

```

2. Multiple row subquery:
    - It use IN,ALL,ANY operator

### Example Ques: Find the empName whoose location is delhi or mumbai
<!-- Find emp name whoose location is delhi or mumbai -->
```sql
SELECT first_name, last_name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location_id IN (
        SELECT location_id
        FROM locations
        WHERE city IN ('Delhi', 'Mumbai')
    )
);

SELECT empname FROM employee
WHERE deptid IN (
    SELECT deptid FROM dept 
    WHERE location IN('delhi','mumbai')
;)
```

# Difference between IN and ANY in SQL

| Operator | Meaning | Example |
|----------|---------|---------|
| **IN**  | Checks if a value **equals any value** in a list or subquery | `SELECT * FROM employees WHERE department_id IN (10,20,30);` |
| **ANY** | Compares a value to **each value in a subquery**; true if **any comparison** is true | `SELECT * FROM employees WHERE salary > ANY (SELECT salary FROM employees WHERE department_id=90);` |

### Quick Tip:
- Use **IN** for equality checks.  
- Use **ANY** for comparisons like >, <, >=, <=.

### Example Question:
Find emp names whoose salary is greater than the salary of HR department
```sql
SELECT empname FROM employee
WHERE salary > ANY(
    SELECT salary FROM employee
    WHERE deptid = 1
);
```
### Question:
Find emp names whoose salary is greater than 


3. Nested row subquery:
    -  
4. Corelated subquery:
    - 