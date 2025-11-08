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