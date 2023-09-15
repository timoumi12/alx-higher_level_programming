#!/usr/bin/python3
'''lists all states with a name starting with N'''
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    stateName = sys.argv[4];
    query = "SELECT * FROM states WHERE name = %s;"
    cur = conn.cursor()
    cur.execute(query, (stateName,))
    data = cur.fetchall()
    for d in data:
        print(d)
    cur.close()
    conn.close()
