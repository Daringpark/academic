select * from articles;

DELETE FROM articles
WHERE id in (
  SELECT id
  FROM articles
  ORDER BY createdAt
  LIMIT 2);
-- TABLE 선언 하지 않고, SELECT TABLE 내에서 createdAt을 기준으로 head(2)를 삭제하는 명령어