-- lists all genres in the database ny their rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_show_ratings ON tv_show_ratings.rate = tv_genres.id
GROUP BY tv_genres.id
ORDER BY rating DESC;
