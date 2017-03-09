#!/usr/bin/python3
'''
This is the '5-filter_cities' module.

5-filter_cities uses MySQLdb to access a database (passed as argv[3])
filters cities matched to given state (argv[4]) and prints the results.

'''
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    test = cur.execute("SELECT cities.name, states.name FROM cities\
     INNER JOIN states ON states.id = cities.state_id\
     AND states.name = %s\
     ORDER BY cities.id ASC", (sys.argv[4],))
    if test == 0:
        print("No injection without protection.")
    cities = []
    for row in cur.fetchall():
        cities.append(row[0])
    print(', '.join(cities))
    cur.close()
    db.close()
