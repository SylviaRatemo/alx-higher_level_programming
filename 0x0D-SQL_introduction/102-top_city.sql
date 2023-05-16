-- top cities
SELECT city, AVG(value) AS "avg_temp" FROM temperatures WHERE month = 7 or month = 8 ORDER BY value DESC;
