-- select all shows that have a genre linked
SELECT s.title, sg.genre_id
	FROM tv_shows s RIGHT JOIN tv_show_genres sg ON sg.show_id = s.id
	ORDER BY s.title, sg.genre_id;
