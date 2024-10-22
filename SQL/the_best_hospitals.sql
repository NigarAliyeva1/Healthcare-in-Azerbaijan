--TOP 5 hospitals
SELECT hospital_name, ratings 
FROM hospitals
ORDER BY ratings DESC
FETCH FIRST 5 ROWS ONLY;
