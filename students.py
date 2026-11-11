import psycopg2


def get_connection():
    """Connect to the students_db database. Change the password to yours."""
    return psycopg2.connect(host="localhost", dbname="students_db", user="postgres", password="comp3005")

conn = get_connection()
print("connected")
conn.close()
