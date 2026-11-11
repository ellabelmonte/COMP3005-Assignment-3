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