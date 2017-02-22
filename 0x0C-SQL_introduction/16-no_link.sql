-- List all records in 'second_table' that have a name value.

SELECT score, name FROM second_table WHERE (name IS NOT NULL AND name != '')
ORDER BY score DESC;
