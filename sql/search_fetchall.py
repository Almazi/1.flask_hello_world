import sqlite3

with sqlite3.connect("new.db") as connection:

    c = connection.cursor()
    c.execute("SELECT firstname, lastname FROM employees")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1])

    c.close()
