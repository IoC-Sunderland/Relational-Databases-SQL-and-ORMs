import sqlite3

# Connect to the database
connection = sqlite3.connect("college_database.db")

# Create a cursor
cursor = connection.cursor()

# Write your SQL query
sql_command = """INSERT INTO students (student_number,student_name)
    VALUES (33289,"Susan Smith"),
           (67830,"Bob Martin");"""

# Execute your command
cursor.execute(sql_command)

# Commit
connection.commit()

