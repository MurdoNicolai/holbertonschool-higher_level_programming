-- displays all genres of the show dexter
SELECT g.name
	FROM tv_genres g
	RIGHT JOIN tv_show_genres sg ON g.id = sg.genre_id
	RIGHT JOIN tv_shows s ON sg.show_id = s.id
	WHERE title = 'Dexter'
	ORDER BY g.name;

