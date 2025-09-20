-- Assuming dataset is already present in our system

-- Q. Upper Lower()
SELECT emp_name,
    UPPER(emp_name) AS name_upper,
    LOWER(emp_name) AS name_lower
FROM emp;

-- Retreive empname from emp table in captial letters with length
SELECT 
    UPPER(emp_name) AS emp_name_upper,
    LENGTH(emp_name) AS name_length
FROM emp;

-- Aggregate Function(sum,avg,max(),count)
-- eg queries 
SELECT SUM(salary) AS total_salary
FROM emp;


-- Q. Calculate avg salary of department greater than 40000
SELECT dept_id, AVG(salary) AS avg_salary
FROM emp
GROUP BY dept_id
HAVING AVG(salary) > 40000;


-- Q. Write avg salary of department greater than 40000
SELECT department_id,AVG(salary) AS avg_salary 
FROM employees
Group BY department_id HAVING avg(salary) >40000;