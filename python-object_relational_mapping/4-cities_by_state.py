#!/usr/bin/python3
"""
this is global enviroment
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """
        this is local enviroment
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
