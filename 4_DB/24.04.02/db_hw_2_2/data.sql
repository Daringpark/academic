
CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE,
  total_amount REAL
);

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT,
  phone TEXT
);

-- 데이터 채워넣기 (orders)
INSERT INTO
  orders(order_date, total_amount)
VALUES
  ('2023-07-15', 50.99),
  ('2023-07-16', 75.5),
  ('2023-07-17', 30.25);

-- 데이터 채워넣기 (customers)
INSERT INTO
  customers(name, email, phone)
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('이철수', 'lee.cheolsu@example.com', '010-2222-5555');

-- 데이터 수정 (삭제)
DELETE FROM orders
WHERE order_id == 3;
-- 데이터 수정 (내용 수정)
UPDATE customers SET name = '홍길동'
WHERE customer_id == 1;

SELECT *  FROM customers;
SELECT *  FROM orders;