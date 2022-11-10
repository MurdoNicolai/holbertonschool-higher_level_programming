--  lists all cities contained in the database  with their States
SELECT c.id, c.name, s.name
	FROM cities c
	JOIN states s ON c.state_id = s.id
	ORDER BY c.id
