import psycopg2
import read
conn = psycopg2.connect(dbname='test1', user='akatruk', 
                        password='Vfhnvfhn123', host='localhost')
cursor = conn.cursor()
# cursor.execute(read.input_to_db)
# cursor.execute(read.input_to_db)
print(read.output_api())

cursor.close()
conn.close()
()

f = open('out.txt', 'r+')
f.truncate(0)