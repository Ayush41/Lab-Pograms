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

-- Aggregate Function


-- Q. Calculate avg salary of department greater than 40000
SELECT dept_id, AVG(salary) AS avg_salary
FROM emp
GROUP BY dept_id
HAVING AVG(salary) > 40000;
