#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query
    query = "SELECT * FROM states ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch all results
    states = cursor.fetchall()

    # Print results in required format
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
