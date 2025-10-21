-- List all records with a non-empty name, show score then name, ordered by score desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
  AND TRIM(name) <> ''
ORDER BY score DESC;