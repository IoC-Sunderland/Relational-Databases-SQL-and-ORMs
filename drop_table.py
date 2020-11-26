import sqlite3

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Drop the table
cursor.execute("DROP TABLE students;")

