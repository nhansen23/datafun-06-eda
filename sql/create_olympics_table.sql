-- Drop joined tables if table exists
DROP TABLE IF EXISTS olympic_data;

CREATE TABLE olymic_data
AS
SELECT ID as athlete_id, name, gender, age, team, athletes.noc, 
games, year, season, city, sport, event, medal, region
FROM athletes 
INNER JOIN countries
ON athletes.noc = countries.noc;