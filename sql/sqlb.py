import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO population VALUES ('CALI', \'CA', 80000) ")
    cursor.execute("INSERT INTO population VALUES ('LAS VEGAS', \'CA', 900000) ")

    conn.commit()
except sqlite3.OperationalError:
    print("Table name damnit")

conn.close()
