
-- 조회 하기
SELECT * FROM users;

-- 18세 미만 유저 조회 하기
SELECT * FROM users WHERE age < 18;

-- 18세 미만 age, phone 조회 하기
SELECT age, phone FROM users WHERE age < 18;