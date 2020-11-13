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

SELECT * FROM netflix_titles where show_id >80000000;



SELECT * FROM netflix_titles INNER JOIN Netflix_Shows ON 
netflix_titles.title = Netflix_Shows.title;

SELECT count(type) FROM netflix_titles INNER JOIN netflix_shows ON netflix_title.tittle = netflix_shows.title where ratingLevel is Not NULL;

SELECT SUM(duration) FROM netflix_titles where type="Movie";

select count(type_) from netflix_titles inner join netflix_show on netflix_titles.title = netflix_show.title where rating_level is not null ;

SELECT count(title) FROM netflix_titles INNER JOIN netflix_shows ON netflix_titles.title = netflix_shows.title where release year > 2016;

ALTER TABLE netflix_shows DROP rating;
