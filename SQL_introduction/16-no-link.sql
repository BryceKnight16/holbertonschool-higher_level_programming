-- list all records secondtable without name in desc
SELECT score,name FROM second_table
       WHERE name IS NOT NULL
       ORDER BY score DESC;
