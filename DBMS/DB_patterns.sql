CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE departments (
	department_id INT PRIMARY KEY,
	department_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(100) NOT NULL,
	salary DECIMAL(10, 2) NOT NULL,
	department_id INT NOT NULL,
	FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Sales'),
(3, 'Human Resources');

INSERT INTO employees (employee_id, employee_name, salary, department_id) VALUES
(1, 'Ava', 80000.00, 1),
(2, 'Noah', 72000.00, 1),
(3, 'Mia', 68000.00, 1),
(4, 'Liam', 65000.00, 1),
(5, 'Emma', 60000.00, 1),
(6, 'Oliver', 55000.00, 1),
(7, 'Sophia', 70000.00, 2),
(8, 'Ethan', 50000.00, 2),
(9, 'Isabella', 45000.00, 3);

-- 1. Find employees earning more than the average salary.

-- 2. Find departments with more than 5 employees.

-- 3. Join employees with their departments.
