-- lists all cities of california that is found in database
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'california')
ORDER BY id ASC;

