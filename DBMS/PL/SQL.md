# PL/SQL Queries


## PL/SQL Query to check number is ODD or EVEN

### *Solution:-0*
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