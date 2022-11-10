-- list all shows with their corresponding genres
SELECT s.title, g.name
	FROM tv_shows s
	RIGHT JOIN tv_show_genres sg ON s.id = sg.show_id
	RIGHT JOIN tv_genres g ON sg.genre_id = g.id
	ORDER BY s.title, g.name;
