import sqlite3

con = sqlite3.connect("cars.db")

curs = con.cursor()

curs.execute("""CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)""")

con.close()
