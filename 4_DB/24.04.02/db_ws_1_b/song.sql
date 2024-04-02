
-- Search
SELECT * FROM songs;

-- Sort descending
SELECT * FROM songs ORDER BY title DESC;

-- Filtering
SELECT * FROM songs WHERE genre LIKE '%P';

-- Filtering with conditions
SELECT * FROM songs WHERE duration/60 >= 3;