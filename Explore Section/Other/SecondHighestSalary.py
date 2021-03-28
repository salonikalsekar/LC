# Write your MySQL query statement below


SELECT (
SELECT DISTINCT Salary from Employee order by salary desc limit 1 offset 1) as SecondHighestSalary