from connectDB import *
import readstudent
import time

#subroutine/function
def update():
    #use primary key to update a record
    idField = input("Enter the studentID of the record to be updated: ")

    #field to be updated: studentID,name, age, gender,email
    fieldName = input("Enter studentID,name, age, gender,email as field name: ").title()

    # fieldValue: ask for the value for the field to be updated
    fieldValue = input(f"Enter the value for {fieldName} field: ")
    # print(fieldValue)

    # add single quote on either side of string
    fieldValue = "'" + fieldValue + "'" 
    # print(fieldValue)

    # update a record in students table
    " UPDATE films SET {studentID,name, age, gender,email} = {fieldValue for studentID,name, age, gender,email} WHERE filmID ={1/2/3/4/5..}                "
    dbCursor.execute(F"UPDATE students SET {fieldName} = {fieldValue} WHERE studentID = {idField} ")
    dbCon.commit()# save changes to the db table permanently
    print(f"Record {idField}: {fieldValue} updated in the students table")

    # read from db
    # call/invoke the sleep method from the time module 
    time.sleep(3) # Delay execution(code block below) for a given number of seconds

    # call/invoke the read subroutine/function from the readstudent module
    readstudent.read()

if __name__=="__main__":
    update()