-- 2.1
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

-- 2.2
-- 1, 2. species 열 추가 및 데이터 추가
ALTER TABLE zoo ADD species;
UPDATE zoo SET species = 'Panthera leo' WHERE name == 'Lion';
UPDATE zoo SET species = 'Loxodonta africana' WHERE name == 'Elephant';
UPDATE zoo SET species = 'Giraffa cameloparadalis' WHERE name == 'Giraffe';
UPDATE zoo SET species = 'Cebus capucinus' WHERE name == 'Monkey';

-- 3. height 값을 곱해준다.
UPDATE zoo
SET height = height * 2.54;

-- 4. 데이터 출력
SELECT * FROM zoo;