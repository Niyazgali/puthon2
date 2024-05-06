import psycopg2

# Connect to the database and get the connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='example', 
    user='postgres', 
    password='1234'
    )

# Create a cursor to work with our DB
cur = conn.cursor()

cur.execute('DROP TABLE examp_data')

conn.commit()


cur.execute("""CREATE TABLE examp_data(
            name VARCHAR(10),
            id VARCHAR(10) PRIMARY KEY,
            study_year INT
);
""")

conn.commit()


cur.execute("""INSERT INTO examp_data(name, id, study_year) VALUES
            ('chara', '23b031555', 1),
            ('erke', '23b030888', 2)
""")

conn.commit()

cur.execute("""UPDATE examp_data
            SET study_year = 1
            
""")

conn.commit()


cur.execute("""DELETE FROM examp_data
            WHERE name = 'chara'
            
""")

conn.commit()