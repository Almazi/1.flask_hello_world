import sqlite3

with sqlite3.connect("new.db") as connection:

    c = connection.cursor()

    c.execute("UPDATE population SET population = 908000 where city = 'NYC'")

    c.execute("DELETE FROM population WHERE city = 'BOSTON'")

    print("new data: \n")

    c.execute("SELECT * FROM population")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
    c.close()
