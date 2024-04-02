
-- 1.
SELECT * FROM users WHERE age < 18 ORDER BY age DESC;

-- 2.
SELECT last_name, age FROM (SELECT last_name, age FROM users WHERE age < 18 ORDER BY age DESC) ORDER BY last_name ASC;

-- 3.
SELECT DISTINCT last_name, age FROM (SELECT last_name, age FROM users WHERE age < 18 ORDER BY age DESC) ORDER BY last_name ASC;
