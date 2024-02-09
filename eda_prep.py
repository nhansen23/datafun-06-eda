'''
This script will create the database for the Olympic
EDA.  The database will contain two tables: one for
athletes and their events and another table for a 
country reference.
'''

# Import Standard Libraries
import pathlib

# Import External Libaries
import sqlite3
import pandas as pd


# Define the database file in the current root project directory
db_file = pathlib.Path("olympics.db")

def create_database():
    """Function to create the Olympic database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)


def create_tables():
    '''Function to read and execute SQL statements to create tables'''
    try:
        with sqlite3.connect(db_file) as conn:
                sql_file = pathlib.Path("sql", "create_tables.sql")
                with open(sql_file, "r") as file:
                    sql_script = file.read()
                conn.executescript(sql_script)
                print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:",e)