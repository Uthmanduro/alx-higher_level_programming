-- lists all records with a score >= 10 in the second table
select score, name from second_table
where score >= 10
order by score desc;
