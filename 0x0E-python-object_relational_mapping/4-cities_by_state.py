#!/usr/bin/python3
'''
This is the '4-cities_by_state' module.

4-cities_by_state uses MySQLdb to access a database (passed as argv[3])
lists all cities and prints the results.

'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
