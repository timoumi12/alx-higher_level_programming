#!/usr/bin/python3
'''lists all cities from the database hbtn_0e_4_usa'''
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
    stateName = sys.argv[4]
    query = "SELECT cities.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s;"
    cur = conn.cursor()
    cur.execute(query, (stateName,))
    data = cur.fetchall()
    states = []
    for d in data:
        states.append(d[0])
    print(", ".join(states))
    cur.close()
    conn.close()
