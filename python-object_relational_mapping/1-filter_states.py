#!/usr/bin/python3
"""Lists states starting with N."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' "
                "ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
