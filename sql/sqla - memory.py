#Create sql lite database and table

#import sqlite3

import sqlite3

#create a new database if the database doesnt exist
conn = sqlite3.connect(":memory:")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table

cursor.execute("""CREATE TABLE population(city TEXT, state TEXT, population INT)""")

conn.close()
