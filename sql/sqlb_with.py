import sqlite3

with sqlite3.connect("new.db") as connection: #with as connection to avoid conn.commit()

    c = connection.cursor()

    c.execute("INSERT INTO population VALUES ('CALI', \'CA', 80000) ")

    c.execute("INSERT INTO population VALUES ('LAS VEGAS', \'CA', 900000) ")

#conn.commit()

    c.close()
