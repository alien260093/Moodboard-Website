import sqlite3 as sql

def listExtension():
  con = sql.connect("Database/data_source.db")
  cur = con.cursor()
  data = cur.execute('SELECT * FROM Moodboards').fetchall()
  con.close()
  return data
