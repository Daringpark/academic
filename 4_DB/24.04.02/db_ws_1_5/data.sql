
-- 1.
SELECT * FROM users WHERE age >= 30 AND balance >= 1000;

-- 2.
SELECT * FROM
(SELECT * FROM users WHERE balance <= 1000)
WHERE age <= 20;

-- 3.
SELECT * FROM 
(SELECT * FROM users WHERE first_name LIKE '현%' AND country LIKE '제주특별%')
WHERE age == (SELECT MAX(age) FROM users WHERE first_name LIKE '현%' AND country LIKE '제주특별%');

-- 4.
SELECT * FROM 
(SELECT * FROM users WHERE last_name LIKE '박%' AND age >= 25)
WHERE age == (SELECT MIN(age) FROM users WHERE last_name LIKE '박%' AND age >= 25);

-- 구조 단순화
SELECT * FROM 
(SELECT * FROM users WHERE last_name LIKE '박%' AND age >= 25)
ORDER BY age ASC
LIMIT 1;

-- 5.
-- 구조가 복잡해짐
SELECT * FROM 
(SELECT * FROM users WHERE first_name == '재은' OR first_name == '영일')
WHERE balance == (SELECT MAX(balance) FROM users WHERE first_name == '재은' OR first_name == '영일');

-- ORDER BY와 LIMIT(HEAD)를 이용해서 내가 원하는 데이터를 뽑아낼 수 있음.
SELECT *
FROM users
WHERE first_name == '재은' OR first_name == '영일'
ORDER BY balance DESC
LIMIT 1;

-- 6.
SELECT first_name, last_name, age, phone, country, MAX(balance) AS max_balance
FROM users
GROUP BY country
-- WHERE == 조건문으로 사용함, HAVING == GROUP BY와 함께 사용함
HAVING balance == MAX(balance)
ORDER BY balance DESC;

-- 7.
SELECT *
FROM (SELECT * FROM users
WHERE age >= 30 AND
balance >= (SELECT AVG(balance) FROM users WHERE age >= 30));