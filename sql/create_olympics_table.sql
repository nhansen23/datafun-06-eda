-- Drop joined tables if table exists
DROP TABLE IF EXISTS olympicData;

CREATE TABLE olympicData AS
    SELECT ID AS athlete_id, name AS athlete_name, Sex AS gender, age, team, athletes.noc AS NOC, games, year, season, city, sport, event, medal, region
    FROM athletes
    INNER JOIN countries ON athletes.noc = countries.noc;