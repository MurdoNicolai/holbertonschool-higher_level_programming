-- displays all genres of the show dexter
SELECT g.name
	FROM tv_genres g
	RIGHT JOIN tv_show_genres sg ON g.id = sg.genre_id
	WHERE show_id = (
		SELECT id
				FROM tv_shows
				WHERE title = 'Dexter'
	)
	ORDER BY g.name;

