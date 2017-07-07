# Write your MySQL query statement below
select w1.Id from Weather w1, Weather w2 where w1.Temperature > w2.Temperature and SUBDATE(w1.Date, 1) = w2.Date;
