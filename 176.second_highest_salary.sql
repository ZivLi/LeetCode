SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (           # WHERE Salary NOT IN (  
   SELECT MAX(Salary)
   FROM Employee
);
