# database.py
import mysql.connector
from mysql.connector import Error

config = {
    'host': 'localhost',       # Replace with your MySQL server host
    'user': 'root',            # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'database': 'emp_db'      # Replace with your database name
}

def connect():
    """Establishes a connection to the database."""
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

def create_table():
    """Creates the employees table in the database if it doesn't exist."""
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT,
                department VARCHAR(255)
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()
