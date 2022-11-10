-- dislplays TV Show genre and Number of shows linked to this genre
SELECT g.name, count(sg.show_id)
	FROM tv_genres g
	RIGHT JOIN tv_show_genres sg ON g.id = sg.genre_id
	GROUP BY genre_id
	ORDER BY count(sg.show_id) DESC;
