-- lists all shows without  the genre comedy in the database
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT
	tv_shows.id FROM tv_shows
	JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
	JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC;
