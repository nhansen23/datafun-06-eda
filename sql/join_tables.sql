-- Create a single data source for EDA
SELECT ID as athlete_id, name, gender, age, team, athletes.noc, 
games, year, season, city, sport, event, medal, region
FROM athletes 
INNER JOIN countries
ON athletes.noc = countries.noc