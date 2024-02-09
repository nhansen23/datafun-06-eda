'''
This script will create the database for the Olympic
EDA.  The database will contain two tables: one for
athletes and their events and another table for the 
country references.

This script will also populate the athletes and countries
tables with the date in the CSV files.
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

def insert_data_from_csv():
    '''Function to use pandas to read data from CSV files
       and insert the records into their respective tables'''
    try:
        athletes_data_push = pathlib.Path("data","athlete_events.csv")
        countries_data_push = pathlib.Path("data","country_definitions.csv")
        athletes_df = pd.read_csv(athletes_data_push)
        countries_df = pd.read_csv(countries_data_push)
        with sqlite3.connect(db_file) as conn:
            athletes_df.to_sql("athletes", conn, if_exists="replace", index=False)
            countries_df.to_sql("countries", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except(sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)


def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()