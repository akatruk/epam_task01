# epam_task01
API https://covidtracker.bsg.ox.ac.uk/about-api 
    https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2020-01-01/2020-05-01

show_result.py
read from API -> insert to file -> load to database PostgreSQL -> run Flask with selected table 'scripts/increment_data_load.sql'

test_show_result.py
unittest: check to database PostgreSQL connectivity

