-- list all comedy shows
SELECT s.title
	FROM tv_shows s
	RIGHT JOIN tv_show_genres sg ON s.id = sg.show_id
	RIGHT JOIN tv_genres g ON sg.genre_id = g.id
	WHERE name = 'Comedy'
	ORDER BY s.title;
