# Write your MySQL query statement below
select a.customer_id, count(a.visit_id)  count_no_trans  from visits a left join transactions b on a.visit_id=b.visit_id where b.visit_id is null group by a.customer_id


