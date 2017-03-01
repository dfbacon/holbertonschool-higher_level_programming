-- Show all comedy shows from hbtn_0d_tvshows.

SELECT tv_shows.title FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_show.id
WHERE tv_genres.name = 'Comedy' ORDER BY tv_show.title ASC;
