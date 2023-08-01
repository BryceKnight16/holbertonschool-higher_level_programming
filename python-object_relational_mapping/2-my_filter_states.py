#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    searched_name = sys.argv[4]
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE BINARY name LIKE '{searched_name}';")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
