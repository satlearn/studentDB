from connectDB import *  

#subroutine/function

def read():
    dbCursor.execute("SELECT * FROM students")
    records = dbCursor.fetchall()
    for aRecord in records: 
        print(aRecord)
if __name__=="__main__":
    read()


