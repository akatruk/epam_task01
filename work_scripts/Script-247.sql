drop table epam;
create table epam
(
id serial,
country_code varchar null,
date_value date null,
confirmed varchar null,
deaths varchar null,
stringency_actual numeric(10, 5) null,
stringency numeric(10, 5) null
)

select * from epam;
truncate table epam;

select *
from epam e
order by deaths::int desc;

