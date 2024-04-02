

-- 테이블 그룹화
SELECT genre, COUNT(genre) AS count FROM songs GROUP BY genre;

-- 집계 함수
SELECT genre, COUNT(genre) AS count, AVG(duration) AS average_duration FROM songs GROUP BY genre;