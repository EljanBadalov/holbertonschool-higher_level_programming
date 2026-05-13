#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Terminal arqumentlərini qəbul edirik
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Verilənlər bazasına qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Kursor obyekti yaradırıq
    cursor = db.cursor()

    # Sorğunu icra edirik (Sıralama vacibdir: ORDER BY id ASC)
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Bütün nəticələri alırıq
    query_rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in query_rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
