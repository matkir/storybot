import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('storyteller.db') # Creates a new database file if it doesn't exist
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    try:
        sql_create_stories_table = """ CREATE TABLE IF NOT EXISTS Stories (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        title text NOT NULL,
                                        content text NOT NULL,
                                        last_updated datetime NOT NULL
                                    ); """
        conn.execute(sql_create_stories_table)
    except Error as e:
        print(e)

def main():
    conn = create_connection()

    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()