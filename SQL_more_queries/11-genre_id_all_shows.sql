-- select all shows with their genre id
SELECT s.title, sg.genre_id
	FROM tv_shows s LEFT JOIN tv_show_genres sg ON sg.show_id = s.id
	ORDER BY s.title, sg.genre_id;
