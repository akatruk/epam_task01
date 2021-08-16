path = 'scripts/increment_data_load.sql'
 
try:
    open(path, 'w').close()
except IOError:
    print('Failure')