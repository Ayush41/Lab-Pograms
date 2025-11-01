-- Subqueries Programs of oracle dbms

-- ### LAB QUESTIONS
-- Creating Employees Table with constraint Foeignkey using department table
CREATE TABLE employees (
    empid NUMBER PRIMARY KEY,                     
    empname VARCHAR2(100) NOT NULL,               
    empemail VARCHAR2(100) UNIQUE,                
    salary NUMBER CHECK (salary >= 30000),        
    deptid NUMBER,                                
    joindate DATE DEFAULT SYSDATE,                
    CONSTRAINT fk_dept FOREIGN KEY (deptid)
        REFERENCES departments(department_id)
);

--  Inserting values in the table
INSERT INTO employees (empid, empname, empemail, salary, deptid, joindate)
VALUES (101, 'Alice Johnson', 'alice.johnson@example.com', 50000, 1, TO_DATE('15-JAN-2023','DD-MON-YYYY'));

INSERT INTO employees (empid, empname, empemail, salary, deptid, joindate)
VALUES (102, 'Bob Smith', 'bob.smith@example.com', 60000, 2, TO_DATE('10-JUN-2022','DD-MON-YYYY'));

INSERT INTO employees (empid, empname, empemail, salary, deptid, joindate)
VALUES (103, 'Charlie Brown', 'charlie.brown@example.com', 70000, 3, TO_DATE('22-SEP-2021','DD-MON-YYYY'));

INSERT INTO employees (empid, empname, empemail, salary, deptid, joindate)
VALUES (104, 'David Will', 'david.will@example.com', 55000, 1, TO_DATE('05-DEC-2022','DD-MON-YYYY'));

INSERT INTO employees (empid, empname, empemail, salary, deptid, joindate)
VALUES (105, 'Eye Carter', 'eye.carter@example.com', 65000, 2, TO_DATE('20-MAR-2023','DD-MON-YYYY'));


-- find an emp name whoose salary is greater than avg salary
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);


-- Find employees who work in the IT department
SELECT empid, empname, salary
FROM employees
WHERE deptid = (
    SELECT department_id
    FROM departments
    WHERE department_name = 'IT'
);

-- Find the highest salary in the company
SELECT MAX(salary) AS highest_salary
FROM employees;


-- find the second-highest salary in the company
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Find employees who joined before the most recent joining date
SELECT empid, empname, joindate
FROM employees
WHERE joindate < (SELECT MAX(joindate) FROM employees);

-- FInd employees who do not belong to any department
SELECT empid, empname
FROM employees
WHERE deptid NOT IN (
    SELECT department_id
    FROM departments
);
