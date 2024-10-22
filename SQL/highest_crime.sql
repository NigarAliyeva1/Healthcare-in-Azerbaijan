--TOP 5 highest crime percentage 2023
with top_5 as (
SELECT c.region_id,c.region,round(c.year_2023/p.people_count *100,5) as percentage_of_crime
FROM crime c
left join population p on c.region_id=p.region_id
ORDER BY percentage_of_crime DESC
FETCH FIRST 5 ROWS ONLY)

select t.region,count(h.hospital_id) as count_of_hospitals,t.percentage_of_crime  
from top_5 t
left join  hospitals h  on h.region_id=t.region_id
group by t.region,percentage_of_crime
order by t.percentage_of_crime desc
