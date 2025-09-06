import sqlite3 as sql

def listExtension():
    con = sql.connect("Database/data_source.db")
    cur = con.cursor()

    # Run query
    data = cur.execute('SELECT * FROM Moodboards').fetchall()

    # Print raw DB data for debugging
    print("DB query results:", data)

    con.close()
    return data