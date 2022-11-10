-- displays all films that aren't comedy
SELECT s2.title
	FROM tv_shows s2
	LEFT JOIN(
		SELECT s.title, g.name
			FROM tv_shows s
			RIGHT JOIN tv_show_genres sg ON s.id = sg.show_id
			RIGHT JOIN tv_genres g ON sg.genre_id = g.id
			WHERE name = 'Comedy'
		) AS ComedyTable
	ON s2.title = ComedyTable.title
	WHERE name IS NULL
	ORDER BY s2.title;

