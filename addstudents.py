from connectDB import *
import readstudent
import time

def insert_student():
    studentID = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    gender= input("Enter student gender: ")
    email = input("Enter student email: ")

    student_data = (studentID,name,age,gender,email)

    dbCursor.execute("INSERT INTO students(studentID,name,age,gender,email) VALUES (?,?,?,?,?)", student_data)
    dbCon.commit()  

    print(f"{name} inserted into the students")

    time.sleep(3)  # Delay execution(code block below) for a given number of seconds

    # Call/invoke the read subroutine/function from the readfilm module
    readstudent.read()

if __name__ == "__main__":
    insert_student()

