import pymysql

conn = pymysql.connect(
    host='sql6.freesqldatabase.com',
    database='sql6432733',
    user='sql6432733',
    password='MTTiE8MquJ',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

sql_query = """ CREATE TABLE course (
    id integer AUTO_INCREMENT PRIMARY KEY,
    name text NOT NULL,
    likes integer NOT NULL
)"""

cursor.execute(sql_query)
conn.close()
