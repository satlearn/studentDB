import connectDB
import readstudent
import time

#subroutine/function
def delete():
     #use primary key to delete a record
    idField = input("Enter the filmID of the record to be deleted: ")

    "DELETE FROM songs WHERE studentID = 1/2/3/4/5/......"
    connectDB.dbCursor.execute(f"DELETE FROM students WHERE studentID = {idField}")
    connectDB.dbCon.commit()

    print(f"Record {idField} deleted from the students table")

    # read from db
    # call/invoke the sleep method from the time module 
    time.sleep(3) # Delay execution(code block below) for a given number of seconds

    # call/invoke the read subroutine/function from the readstudent module
    readstudent.read()


if __name__=="__main__":
    delete()




    