import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()

def jokesFromTable():
  c.execute("Select joke from jokes_entries")
  joke_list = c.fetchall()
  return joke_list

# print(jokesFromTable())
conn.commit()

def closeConnection():
  conn.close()
