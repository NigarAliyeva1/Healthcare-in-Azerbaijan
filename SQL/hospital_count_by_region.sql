--hospital count by every region
SELECT region, COUNT(*) AS hospital_count
FROM hospitals
GROUP BY region
ORDER BY hospital_count DESC;
