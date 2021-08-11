import requests

url = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2020-05-01/2020-05-31"
response = requests.get(url, headers={'Accept':'application/json'})
data = response.json()
data1 = data['data']['2020-05-11']

def output_api():
    k = ''
    for i in data1.items():
        k += 'INSERT INTO epam (country_code, date_value, confirmed, deaths, stringency_actual, stringency) VALUES (' + "'"+ i[1]['country_code'] + "'" + ', ' + "'"+ i[1]['date_value'] + "'" + ", " + "'"+ str(i[1]['confirmed']) + "'" + ", " + "'"+ str(i[1]['deaths']) + "'" + ", " + "'"+ str(i[1]['stringency_actual']) + "'"+ ", " + "'"+ str(i[1]['stringency']) + "'"+ ');'
    return k

# with open('out.txt', 'w') as f:
#      f.write(output_api())

f = open('out.txt', 'r+')
f.truncate(0)