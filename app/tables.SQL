-- Each saved tree needs:

-- location
-- ranking

-- hover name
-- hover data



-- Add users:
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL);
CREATE UNIQUE INDEX username ON users (username);

