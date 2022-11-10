-- select all shows without a genre linked
SELECT s.title, sg.genre_id
	FROM tv_shows s LEFT JOIN tv_show_genres sg ON sg.show_id = s.id
	WHERE sg.genre_id IS NULL
	ORDER BY s.title;
