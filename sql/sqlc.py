import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    cities = [('BOSTON', 'MA', 55), ('CHICGO','IL', 660000), ('HOUSTON', 'TX', 100000), ('PHOENIX', 'AZ', 985006)]
    c.executemany('INSERT INTO population VALUES (?, ?, ?)', cities)

    c.close()
