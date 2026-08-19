import sqlite3

# creation of database

stock = sqlite3.connect("practice.db")
cursor = stock.cursor()

#cursor will start ur 

#creating table
#makes it start at the first upper corner
cursor.execute(
"""

CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
    
)
"""
)

stock.commit()
stock.close()


print("Table created successfully...")