-- group records by score and display the number of groups
SELECT score, COUNT (*) AS number FROM second_table
       GROUP BY score
       GROUP BY	number DESC;
