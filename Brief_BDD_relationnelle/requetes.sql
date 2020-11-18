#sudo mysql --local-infile=1 -u root

DROP TABLE IF EXISTS netflix_titles;

CREATE TABLE netflix_titles( 
  show_id INT NOT NULL,
  type VARCHAR(10),
  title VARCHAR(110),
  director VARCHAR(210),
  cast VARCHAR(780),
  country VARCHAR(130),
  date_added VARCHAR(20),
  release_year INT NOT NULL,
  rating VARCHAR(10),
  duration VARCHAR(10),
  listed_in VARCHAR(80),
  description VARCHAR(280),
  PRIMARY KEY(show_id)
  );
 
 
LOAD DATA LOCAL INFILE 'netflix_titles.csv'
INTO TABLE netflix_titles 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

CREATE TABLE netflix_shows (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(64),
    rating VARCHAR(9),
    ratingLevel VARCHAR(126),
    ratingDescription INT NOT NULL,
    `release year` INT NOT NULL,
    `user rating score` VARCHAR(4),
    `user rating size` INT NOT NULL,
    PRIMARY KEY(id)
);


LOAD DATA LOCAL INFILE 'netflix_shows.csv' 
	INTO TABLE netflix_shows
	CHARACTER SET latin1
	FIELDS TERMINATED BY ',' 
	ENCLOSED BY '"'
	LINES TERMINATED BY '\r'
	IGNORE 1 LINES(title, rating, ratingLevel, ratingDescription,`release year`, `user rating score`, `user rating size`
);

SELECT * FROM netflix_titles where show_id >80000000;	#6



SELECT * FROM netflix_titles INNER JOIN Netflix_Shows ON 
netflix_titles.title = Netflix_Shows.title;

SELECT count(type) FROM netflix_titles INNER JOIN netflix_shows ON netflix_title.tittle = netflix_shows.title where ratingLevel is Not NULL;

SELECT SUM(duration) FROM netflix_titles where type="Movie";	#10

select count(type_) from netflix_titles inner join netflix_show on netflix_titles.title = netflix_show.title where rating_level is not null ;	#11	

SELECT count(title) FROM netflix_titles INNER JOIN netflix_shows ON netflix_titles.title = netflix_shows.title where `release year` > 2016;	#12

ALTER TABLE netflix_shows DROP rating;

###################################################correction

SELECT title FROM netflix_titles WHERE show_id<80000000;	#6

SELECT duration FROM netflix_title WHERE type='TV Show';	#7

SELECT t.title FROM netflix_title t, netflix_shows s WHERE t.title = s.title;	#9
SELECT NetflixShows.title 
FROM NetflixShows INNER JOIN NetflixTitle ON NetflixShows.title = NetflixTitle.title 
GROUP BY NetflixShows.title;

SELECT sum(CAST(SUBSTR(duration , 1, 3)) AS INT) from netflix_titles WHERE type = 'Movie';
SELECT sum(CAST(SUBSTR(duration , 1, 3)AS INT)) from netflix_titles WHERE type = 'Movie';
SELECT SUM(CAST(duration AS INT))
FROM netflix_titles
WHERE type='Movie' ;

SELECT sum(SUBSTR(duration, 1, 3)) from netflix_titles WHERE type = 'Movie';	#10
SELECT SUM(duration) FROM netflix_titles where type="Movie";

SELECT count(distinct s.title)	#11		
from netflix_shows as s
INNER JOIN netflix_titles as t
ON s.title = t.title
WHERE ratingLevel<>''AND type='TV Show';

SELECT COUNT(DISTINCT netflix_titles.title)
FROM netflix_titles 
INNER JOIN netflix_shows 
ON netflix_titles.title = netflix_shows.title
WHERE netflix_shows.release_year > 2016 AND netflix_titles.release_year > 2016;	#12
#AS nb  FROM netflix_title nt, netflix_shows ns WHERE nt.title =  ns.title && nt.release_year = 2016 ;

ALTER TABLE netflix_shows DROP COLUMN rating;	#13

ALTER TABLE netflix_shows ADD id INT NOT NULL AUTO_INCREMENT primary key first	#14
DELETE FROM netflix_shows ORDER BY id DESC LIMIT 100;
DELETE FROM netflix_shows WHERE id BETWEEN 200 AND 300;

UPDATE netflix_shows SET ratingLevel = "it's a comment" WHERE ID = 26 AND title = "Marvel's Iron Fist";	#15






