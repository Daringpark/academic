
-- 1. CREATE DB TABLE
CREATE TABLE zoo(
  name TEXT,
  eat TEXT,
  weight INTEGER,
  height INTEGER,
  age INTEGER
);

-- 2. INSERT INTO
INSERT INTO zoo
(name, eat, weight, height, age)
VALUES
('Lion', 'Meat', 200, 120, 5),
('Elephant', 'Plants', 5000, 300, 15),
('Giraffe', 'Leaves', 1500, 550, 10),
('Monkey', 'Fruits', 50, 60, 8);

-- 3. SELECT
SELECT * FROM zoo;