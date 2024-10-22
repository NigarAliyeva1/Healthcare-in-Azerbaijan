--her 10 000 adama dushen tibb bacisi sayi
with public_hospital_region as ( 
select sum(p.people_count)/10000 as public_hospital_region
from population p)

select round(year_2023/(select * from public_hospital_region)) as nurse_per_10000_people
from orta_ixtisasli_tibb_ishchileri where orta_tibb_ishchileri='tibb bacısı'
