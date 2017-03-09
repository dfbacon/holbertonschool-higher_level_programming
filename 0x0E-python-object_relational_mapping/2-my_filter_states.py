#!/usr/bin/python3
'''
This is the '2-my_filter_states' module.

2-my_filter_states uses MySQLdb to access a database (passed as argv[3])
filters for table.name to match argv[4] and prints the results.

'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states\
    WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
