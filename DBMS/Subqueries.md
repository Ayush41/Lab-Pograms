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
```

2. Multiple row subquery:
    - 

3. Nested row subquery:
    - 
4. Corelated subquery:
    - 