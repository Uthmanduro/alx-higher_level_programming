-- lists the number of records with the smae scores
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
