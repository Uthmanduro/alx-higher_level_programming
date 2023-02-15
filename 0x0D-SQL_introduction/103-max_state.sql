-- displays the max temperature of each state 
SELECT state, MAX(value) AS max_temp from temperatures
GROUP BY state
ORDER BY state ASC;
