--avg number of beds by hospital type
SELECT hospital_type, round(AVG(number_Of_beds),2) AS AvgBeds
FROM hospitals
GROUP BY hospital_type;
