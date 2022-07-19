
# install psycopg2 (if needed)
# pip3 install psycopg2    # (or pip)

# https://www.pg4e.com/code/simple.py

# https://www.pg4e.com/code/hidden-dist.py
# copy hidden-dist.py to hidden.py
# edit hidden.py and put in your credentials

# python3 simple.py

# To check the results, use psql and look at the
# pythonfun table

import psycopg2
import hidden

# Load the secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'], 
        user=secrets['user'], 
        password=secrets['pass'], 
        connect_timeout=3)
        
cur = conn.cursor()
number = 236736
value=number
for i in range(300) :
    print(i+1, value)
    txt= str(value)
    sql = 'INSERT INTO pythonseq(val) VALUES (%s);'
    cur.execute(sql, (txt, ))
    value = int((value * 22) / 7) % 1000000


conn.commit()
cur.close()

