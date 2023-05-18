-- Compound SQL Queries
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows FROM tv_genres
WHERE (SELECT tv_Show_genres WHERE tv_genres.id = tv_show_genres.genre_id)GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;
