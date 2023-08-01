import sqlite3 as sql # import the sqlite3 module

dbCon = sql.connect("python_project1/studentDB.db")


dbCursor = dbCon.cursor()

dbCursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    studentID INTEGER PRIMARY KEY,
                    name TEXT ,
                    age INTEGER,
                    gender CHAR(6),
                    email TEXT
                    
                  )''')


dbCon.commit