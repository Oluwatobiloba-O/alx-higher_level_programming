-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
	(SELECT tv_genres.name
	FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	LEFT JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter')
	ORDER BY tv_genres.name;
