INSERT INTO ProductionStudios (StudioID, StudioName, Country, YearFounded)
VALUES
(1, 'Sony Pictures', 'USA', '1989-08-07'), -- The Shawshank Redemption
(2, 'Columbia Pictures', 'USA', '1918-01-10'), -- The Godfather
(3, 'Warner Bros.', 'USA', '1923-04-04'), -- The Dark Knight
(4, 'Miramax Films', 'USA', '1979-10-01'), -- Pulp Fiction
(5, 'Paramount Pictures', 'USA', '1912-05-08'), -- Forrest Gump
(6, 'Village Roadshow Pictures', 'Australia', '1986-04-10'), -- The Matrix
(7, 'Syncopy', 'USA', '2001-01-01'), -- Inception
(8, 'Universal Pictures', 'USA', '1912-04-30'), -- Schindler's List
(9, 'New Line Cinema', 'USA', '1967-03-17'), -- The Lord of the Rings: The Fellowship of the Ring
(10, '20th Century Fox', 'USA', '1935-05-31'); -- Fight Club

INSERT INTO Movies (MovieID_, Title, ReleaseYear, Genre, Duration, Country, PeopleRating, CriticsRating,StudioID)
VALUES
(1, 'The Shawshank Redemption', '1994-09-23', 'Drama', 142, 'USA', 9.1, 9.8, 1),
(2, 'The Godfather', '1972-03-24', 'Crime', 175, 'USA', 8.6, 9.1, 2),
(3, 'The Dark Knight', '2008-07-18', 'Action', 152, 'USA', 9, 9, 3),
(4, 'Pulp Fiction', '1994-10-14', 'Crime', 154, 'USA', 9.5, 9.9, 4),
(5, 'Forrest Gump', '1994-07-06', 'Drama', 142, 'USA', 9.9, 9.9, 5),
(6, 'The Matrix', '1999-03-31', 'Action', 136, 'USA', 8.3, 8.4, 6),
(7, 'Inception', '2010-07-16', 'Sci-Fi', 148, 'USA', 9.3, 9, 7),
(8, 'Schindler''s List', '1993-11-30', 'Biography', 195, 'USA', 8, 9.5, 8),
(9, 'The Lord of the Rings: The Fellowship of the Ring', '2001-12-19', 'Adventure', 178, 'USA', 9.4, 9.3, 9),
(10, 'Fight Club', '1999-10-15', 'Drama', 139, 'USA', 9.5, 9.6, 10);

INSERT INTO Actor (ActorID, FirstName, LastName, BirthYear, Country, MovieID_)
VALUES
(1, 'Tim', 'Robbins', '1958-10-16', 'USA', 1), -- The Shawshank Redemption
(2, 'Marlon', 'Brando', '1924-04-03', 'USA', 2), -- The Godfather
(3, 'Christian', 'Bale', '1974-01-30', 'Wales', 3), -- The Dark Knight
(4, 'John', 'Travolta', '1954-02-18', 'USA', 4), -- Pulp Fiction
(13, 'Samuel Leroy', 'Jackson', '1948-12-21', 'USA', 4), -- Pulp Fiction
(5, 'Tom', 'Hanks', '1956-07-09', 'USA', 5), -- Forrest Gump
(6, 'Keanu', 'Reeves', '1964-09-02', 'Lebanon', 6), -- The Matrix
(7, 'Leonardo', 'DiCaprio', '1974-11-11', 'USA', 7), -- Inception
(8, 'Liam', 'Neeson', '1952-06-07', 'Northern Ireland', 8), -- Schindler's List
(9, 'Elijah', 'Wood', '1981-01-28', 'USA', 9), -- The Lord of the Rings: The Fellowship of the Ring
(10, 'Edward', 'Norton', '1969-08-18', 'USA', 10), -- Fight Club
(11, 'William Bradley', 'Pitt', '1963-12-18', 'USA', 10), -- Fight Club
(12, 'Helena Bonham', 'Carter', '1966-05-26', 'USA', 10); -- Fight Club

INSERT INTO Director (DirectorID, FirstName, LastName, BirthYear, Country, MovieID_)
VALUES
(1, 'Frank', 'Darabont', '1959-01-28', 'France', 1), -- The Shawshank Redemption
(2, 'Francis Ford', 'Coppola', '1939-04-07', 'USA', 2), -- The Godfather
(3, 'Christopher', 'Nolan', '1970-07-30', 'UK', 3), -- The Dark Knight
(4, 'Quentin', 'Tarantino', '1963-03-27', 'USA', 4), -- Pulp Fiction
(5, 'Robert Lee', 'Zemeckis', '1952-05-14', 'UK', 5), -- Forrest Gump
(6, 'Larry', 'Wachowski', '1965-06-21', 'USA', 6), -- The Matrix
(7, 'Robert', 'Wachowski', '1967-12-29', 'USA', 6), -- The Matrix
(8, 'Christopher', 'Nolan', '1970-07-30', 'UK', 7), -- Inception
(9, 'Steven', 'Spielberg', '1946-12-18', 'USA', 8), -- Schindler's List
(10, 'Peter', ' Jackson', '1961-10-31', 'New Zealand', 9), -- The Lord of the Rings: The Fellowship of the Ring
(11, 'David', 'Fincher', '1962-08-28', 'USA', 10); -- Fight Club