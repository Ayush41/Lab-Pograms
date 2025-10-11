CREATE TABLE emp (
    emp_id NUMBER PRIMARY KEY,
    emp_name VARCHAR2(50),
    job VARCHAR2(50),
    hire_date DATE,
    salary NUMBER
);

INSERT INTO emp (emp_id, emp_name, job, hire_date, salary) VALUES (1, 'John Doe', 'Manager', TO_DATE('2020-01-15', 'YYYY-MM-DD'), 55000);
INSERT INTO emp (emp_id, emp_name, job, hire_date, salary) VALUES (2, 'Jane Smith', 'Developer', TO_DATE('2021-03-10', 'YYYY-MM-DD'), 45000);
INSERT INTO emp (emp_id, emp_name, job, hire_date, salary) VALUES (3, 'Robert Brown', 'Tester', TO_DATE('2019-08-20', 'YYYY-MM-DD'), 40000);
INSERT INTO emp (emp_id, emp_name, job, hire_date, salary) VALUES (4, 'Emily Davis', 'Developer', TO_DATE('2022-06-05', 'YYYY-MM-DD'), 47000);
INSERT INTO emp (emp_id, emp_name, job, hire_date, salary) VALUES (5, 'Michael Wilson', 'Manager', TO_DATE('2021-11-22', 'YYYY-MM-DD'), 60000);

