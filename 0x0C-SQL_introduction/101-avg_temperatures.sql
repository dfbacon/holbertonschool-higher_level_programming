-- show average temperature from external sql table dump.

SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
