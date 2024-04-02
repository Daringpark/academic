-- 1. all fields
SELECT * FROM tracks;

-- 2. selected_col
SELECT Name, Milliseconds, Unitprice FROM tracks;

-- 3. genreID
SELECT * FROM tracks WHERE GenreId = 1;

-- 4. ascending
SELECT * FROM tracks ORDER BY Name ASC;

-- 5. head_10
SELECT * FROM tracks LIMIT 10;