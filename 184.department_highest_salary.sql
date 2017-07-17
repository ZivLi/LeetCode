# Write your MySQL query statement below
select d.Name as Department, e.Name as Employee, e.Salary from Department d, Employee e where e.DepartmentId=d.Id and e.Salary = (select max(Salary) from Employee e2 where e2.DepartmentId=d.Id);
