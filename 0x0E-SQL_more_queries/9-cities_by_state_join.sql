-- lists all the citites containde in the database
SELECT cities.id, cities.name, states.name FROM cities, states
where cities.state_id = states.id
ORDER BY cities.id ASC;
