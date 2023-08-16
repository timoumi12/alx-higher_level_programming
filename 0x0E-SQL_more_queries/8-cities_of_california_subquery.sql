-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name from cities
  WHERE cities.state_id =
  (SELECT * FROM states
  WHERE states.name = 'California')
  ORDER BY cities.id ASC;
