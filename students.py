import psycopg2

#connect to database
def get_connection():
    """Connect to the students_db database. Change the password to yours."""
    return psycopg2.connect(host="localhost", dbname="students_db", user="postgres", password="comp3005")

def getAllStudents():
    """Get all students from the table."""
    conn = get_connection() #connect to database
    cur = conn.cursor() #create cursor

    cur.execute("SELECT * FROM students ORDER BY student_id;") #get all students
    for row in cur.fetchall(): #print each student
        print(row)  

    conn.close() #disconnect from database

def addStudent(first_name, last_name, email, enrollment_date):
    """Add a new student to the table."""
    conn = get_connection() 
    cur = conn.cursor()

    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) "
                "VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date)) #insert student
    
    conn.commit() #save changes
    conn.close() #disconnect from database

def updateStudentEmail(student_id, new_email):
    """Update the email address of the student with the given student_id."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id))
    conn.commit()
    conn.close()


def deleteStudent(student_id):
    """Delete the student with the given student_id."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    conn.close()