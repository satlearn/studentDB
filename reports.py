from connectDB import *



def studentID(): # option 1
    idField = input("Enter the studentID of the students to search for:  ")
    dbCursor.execute(f"SELECT * FROM students WHERE studentID  = '{idField}' ")# select all records from students table
    records = dbCursor.fetchall()# fetches all records selected from the students table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)

def name():  # option 2
    nameField = input("Enter the student name to search for:  ")
    dbCursor.execute(f"SELECT * FROM students WHERE name = '{nameField}' ")# select all records from students table
    records = dbCursor.fetchall()# fetches all records selected from the students table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)

def age(): # option 3
    ageField = input("Enter the age to search for:  ")
    dbCursor.execute(f"SELECT * FROM students WHERE age = '{ageField}' ")# select all records from students table
    records = dbCursor.fetchall()# fetches all records selected from the students table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)

def gender(): # option 4
    genderField = input("Enter the gender to search for:  ")
    dbCursor.execute(f"SELECT * FROM students WHERE Title = '{genderField}' ")# select all records from students table
    records = dbCursor.fetchall()# fetches all records selected from the students table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



def email(): # option 5
    emailField = input("Enter the email to search for:  ")
    dbCursor.execute(f"SELECT * FROM students WHERE email = '{emailField}' ")# select all records from students table
    records = dbCursor.fetchall()# fetches all records selected from the students table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



# fieldName = input("Enter Field Name: ")

def readOrder(): # option 6
    # dbCursor.execute(f"SELECT * FROM students ORDER BY {fieldName} DESC")
    # dbCursor.execute(f"SELECT * FROM students ORDER BY studentID DESC")
    # dbCursor.execute(f"SELECT name, Gender FROM students ORDER BY studentID DESC")
    dbCursor.execute(f"SELECT name, Gender FROM students ORDER BY name ASC")
    # dbCursor.execute(f"SELECT * FROM students WHERE Gender = 'f')
    # dbCursor.execute(f"SELECT * FROM students WHERE Title Like 'b%' ")
    # dbCursor.execute(f"SELECT * FROM students WHERE Title Like '%b%' ")
    # dbCursor.execute(f"SELECT * FROM students WHERE Title NOT Like 'b%' ")
       
    #  https://www.w3schools.com/mysql/mysql_like.asp

    records = dbCursor.fetchall()# fetches all records selected from the students table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



if __name__=="__main__":
    # studentID()
    # name()
    # age()
    # gender()
    # email()
    
    readOrder()
  