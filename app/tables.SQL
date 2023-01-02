-- Each saved tree needs:

-- location
-- ranking

-- hover name
-- hover data



-- Add users:
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL);
CREATE UNIQUE INDEX username ON users (username);

CREATE TABLE trees (id INTEGER PRIMARY KEY AUTOCREMENT NOT NULL, latitude TEXT NOT NULL, longitude TEXT NOT NULL, w3w TEXT NOT NULL, grade INTEGER NOT NULL DEFAULT 404) 
