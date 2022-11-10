-- displays all genres not linked to the show dexter
SELECT g2.name
	FROM tv_genres g2
	LEFT JOIN(
		SELECT g.name, s.title
			FROM tv_genres g
			RIGHT JOIN tv_show_genres sg ON g.id = sg.genre_id
			RIGHT JOIN tv_shows s ON sg.show_id = s.id
			WHERE title = 'Dexter'
		) AS dexterTable
	ON g2.name = dexterTable.name
	WHERE title IS NULL
	ORDER BY g2.name
