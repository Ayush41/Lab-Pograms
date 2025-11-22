# PL/SQL Queries


## Ques1. PL/SQL Query to check number is ODD or EVEN

### *Solution:-1*
```sql
DECLARE
    num NUMBER := &num;   -- Input from user
BEGIN
    IF MOD(num, 2) = 0 THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is EVEN');
    ELSE
        DBMS_OUTPUT.PUT_LINE(num || ' is ODD');
    END IF;
END;
/
```

## Ques2. PL/SQL Query to find factorial of a Number
### Solution2:
```sql

```

## Ques3. PL/SQL Query to find largest number among 3 numbers.
### Solution2:
```sql

```