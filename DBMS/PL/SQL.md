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
DECLARE
   num      NUMBER := &input_number;  -- Replace &input_number with the desired number
   fact     NUMBER := 1;
BEGIN
   FOR i IN 1..num LOOP
      fact := fact * i;
   END LOOP;
   
   DBMS_OUTPUT.PUT_LINE('Factorial of ' || num || ' is ' || fact);
END;
/
```

## Ques3. PL/SQL Query to find largest number among 3 numbers.
### Solution2:
```sql
DECLARE
   num1    NUMBER := &num1;  -- Replace &num1 with the first number
   num2    NUMBER := &num2;  -- Replace &num2 with the second number
   num3    NUMBER := &num3;  -- Replace &num3 with the third number
   largest NUMBER;
BEGIN
   IF num1 >= num2 AND num1 >= num3 THEN
      largest := num1;
   ELSIF num2 >= num1 AND num2 >= num3 THEN
      largest := num2;
   ELSE
      largest := num3;
   END IF;
   
   DBMS_OUTPUT.PUT_LINE('The largest number is ' || largest);
END;
/
```