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

-- Q. Count the num of employees in each department.
SELECT dept_id, COUNT(*) AS employee_count
FROM emp
GROUP BY dept_id;

-- Q. Find the total salary paid in each department
SELECT dept_id, SUM(salary) AS total_salary
FROM emp
GROUP BY dept_id;

-- Q. Find the min salary for each department, only showing departments where the min salary is 50000
SELECT dept_id, MIN(salary) AS min_salary
FROM emp
GROUP BY dept_id
HAVING MIN(salary) = 50000;

-- Q. find departments where the totla salary paid is ebtween 100,000 and 200,000
SELECT dept_id, SUM(salary) AS total_salary FROM emp
GROUP BY dept_id
HAVING SUM(salary) BETWEEN 100000 and 200000;

-- Q. Find the number of employees in each department who joined after 2022
SELECT department_id, COUNT(*) AS employee_count
FROM employees
WHERE hire_date > TO_DATE('31-12-2022', 'DD-MM-YYYY')
GROUP BY department_id;


-- Q. Find departments with at least one employer who has not provided an email
SELECT distinct department_id FROM employees
where email is null or email='';