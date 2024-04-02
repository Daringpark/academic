-- initial table setting
CREATE TABLE song (
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  artist TEXT,
  album TEXT,
  genre TEXT,
  duration INTEGER
);
PRAGMA table_info('song');

INSERT INTO
  song('title', 'artist', 'album', 'genre', 'duration')
VAlUES
  ('NEW title', 'artist 1', 'album 1', 'POP', 281),
  ('Song 2', 'artist 2', 'album 2', 'J-POP', 323),
  ('Song 3', 'artist 3', 'album 3', 'HIPHOP', 248),
  ('Song 4', 'artist 4', 'album 4', 'CLASSIC', 543),
  ('Song 5', 'artist 5', 'album 5', 'JAZZ', 512);

-- Update content ('title')
UPDATE song SET title = 'Song 1' WHERE id = 1;