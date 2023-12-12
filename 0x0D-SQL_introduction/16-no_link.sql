-- This script  lists all records of the table second_table,Don’t list rows without a name value in descending order.
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
