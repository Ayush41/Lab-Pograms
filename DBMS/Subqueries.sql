-- Subqueries Programs of oracle dbms


-- find an emp name whoose salary is greater than avg salary
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
