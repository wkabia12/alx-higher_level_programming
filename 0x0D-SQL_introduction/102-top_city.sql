-- display top 3 cities temp during july and aug ordered by temp DESC
SELECT city, AVG(value) AS avg_temp FROM temperatures 
WHERE month Between 7 AND 8 GROUP BY city 
ORDER BY avg_temp DESC LIMIT 3;
