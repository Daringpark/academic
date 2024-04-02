
-- 1. SELECT ALL
SELECT * FROM artists;

-- 2. COUNT
SELECT COUNT(*) FROM artists;

-- 3. name == AC/DC
SELECT * FROM artists WHERE name == 'AC/DC';

-- 4. only col name
SELECT name FROM artists;

-- 5. OR OPERATOR
SELECT * FROM artists WHERE name = 'Gilberto Gil' OR name == 'Ed Motta';

-- 6. SORT
SELECT * FROM artists ORDER BY name DESC;

-- 7. VINICIUS
SELECT * FROM artists WHERE name LIKE 'Vinícius%' LIMIT 2;

-- 8. ARTISTS INDEX 50(0 ~ index 49) - 70 (,21)
SELECT ArtistId FROM artists LIMIT 49, 21;