
--Avg age of patients who didn't call hospital by gender
select gender,called_hospital,
round(avg(age)) as avg_age from patients p
where called_hospital ='No'
group by gender,called_hospital;

--Max age and Avg rate of patients who didn't call hospital by gender
select gender,called_hospital,
round(avg(age)) as max_age,round(avg(hospital_answer_rate),2) as avg_rate from patients p
where called_hospital !='No'
group by gender,called_hospital;
