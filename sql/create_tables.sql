DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS athletes;

--Create athletes table first as it has no foreign keys
CREATE TABLE athletes(
    athlete_id TEXT PRIMARY KEY,
    athlete_name TEXT,
    gender TEXT,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    team TEXT,
    noc TEXT,
    games TEXT,
    year INTEGER,
    season TEXT,
    city TEXT,
    sport TEXT,
    event TEXT,
    medal TEXT
);

-- Create the countries table
CREATE TABLE countries(
    noc TEXT,
    region TEXT,
    notes TEXT,
    FOREIGN KEY (noc) REFERENCES athletes(noc)
);