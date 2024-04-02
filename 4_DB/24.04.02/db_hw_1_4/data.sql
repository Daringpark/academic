-- 1. love
SELECT * FROM tracks WHERE Name LIKE '%love';

-- 2. GenreId 1 and Milliseconds >= 300000, ordered by unitprice descending
SELECT * FROM tracks where GenreId = 1 and Milliseconds >= 300000 ORDER BY UnitPrice DESC;

-- 3. Groupby GenreId counts
SELECT GenreId, COUNT(*) AS TotalTracks FROM tracks GROUP BY GenreId;

-- 4. Groupby GenreId sum Unitprice where sum Unitprice >= 100
SELECT GenreId, SUM(UnitPrice) AS TotalPrice FROM tracks GROUP BY GenreId HAVING TotalPrice >= 100;