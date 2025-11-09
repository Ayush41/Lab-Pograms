-- #create table 
CREATE TABLE departments (
  deptid     NUMBER(10) CONSTRAINT dept_pk PRIMARY KEY,
  deptname   VARCHAR2(20),
  location   VARCHAR2(10)
);

-- Insert values 
INSERT INTO departments (deptid, deptname, location)
VALUES (10, 'sales', 'newyork');

INSERT INTO departments (deptid, deptname, location)
VALUES (20, 'marketing', 'london');

INSERT INTO departments (deptid, deptname, location)
VALUES (30, 'executive', 'newyork');

INSERT INTO departments (deptid, deptname, location)
VALUES (40, 'operations', 'chicago');


SELECT * FROM departments;

CREATE TABLE employees (
  emp_id     NUMBER(10) CONSTRAINT emp_pk PRIMARY KEY,
  emp_name   VARCHAR2(20) CONSTRAINT emp_name_nn NOT NULL,
  salary     NUMBER(10,2) CONSTRAINT emp_salary_ck CHECK (salary >= 30000),
  deptid     NUMBER(10),
  CONSTRAINT emp_dept_fk FOREIGN KEY (deptid)
    REFERENCES departments(deptid)
);

INSERT INTO employees (emp_id, emp_name, salary, deptid)
VALUES (101, 'Alice John', 50000, 10);

INSERT INTO employees (emp_id, emp_name, salary, deptid)
VALUES (102, 'Bob Smith', 60000, 20);

INSERT INTO employees (emp_id, emp_name, salary, deptid)
VALUES (103, 'Charlie Brown', 70000, 10);

INSERT INTO employees (emp_id, emp_name, salary, deptid)
VALUES (104, 'David Williams', 55000, 30);

INSERT INTO employees (emp_id, emp_name, salary, deptid)
VALUES (105, 'Eve Carter', 65000, 20);

INSERT INTO employees (emp_id, emp_name, salary, deptid)
VALUES (106, 'Allen', 75000, 40);

SELECT * FROM employees;

-- ************************Queries*********************************
-- 1. Which employees earn the same salary as the employee with Employee_ID = 101? (Excluding
-- the employee with ID 101 itself).
SELECT emp_id, emp_name, salary
FROM employees
WHERE salary = (
    SELECT salary 
    FROM employees 
    WHERE emp_id = 101
)
AND emp_id <> 101;


-- 2. List the names of all employees who work in a department located in 'New York'.