--Patients who called the hospital but didn't participate in the rating
update patients p
set hospital_answer_rate=0
where called_hospital='Yes' and hospital_answer_rate is null;
commit;


--Who didn't even call
update patients p
set hospital_answer_rate=0
where called_hospital='No' and hospital_answer_rate is null;
