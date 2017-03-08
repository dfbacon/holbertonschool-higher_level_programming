#!/usr/bin/python3
'''
This is the '0-select_states' module.

0-select_states uses MySQLdb to access a database (passed as argv[3]) and
prints the results.

'''
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
db.close()
