# Write your MySQL query statement below
select name as Customers from Customers where Id not in (select CustomerId from Orders);
// 143ms
select Name as Customers from Customers c where not exists(
    select * from Orders o where c.Id = o.CustomerId);
//124ms
