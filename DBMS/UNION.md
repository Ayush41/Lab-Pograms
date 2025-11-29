# 📘 SQL Lab – UNION, INTERSECT, MINUS & Subqueries

This document contains SQL table creation, sample data insertion, and solutions to lab questions involving **UNION**, **INTERSECT**, **MINUS**, and **subqueries**.

---

## 📌 1. Table Creation

```sql
CREATE TABLE departments (
    dept_id NUMBER PRIMARY KEY,
    dept_name VARCHAR2(30),
    location VARCHAR2(30)
);

CREATE TABLE employees (
    emp_id NUMBER PRIMARY KEY,
    emp_name VARCHAR2(30),
    salary NUMBER,
    dept_id NUMBER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

