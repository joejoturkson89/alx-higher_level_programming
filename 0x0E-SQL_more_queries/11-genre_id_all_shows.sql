-- This script lists all shows contained in the database hbtn_0d_tvshows.
SELECT s.title, g.genre_id
FROM tv_show AS s
LEFT JOIN tv_show_genre AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
