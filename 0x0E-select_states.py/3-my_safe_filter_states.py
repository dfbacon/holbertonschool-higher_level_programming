#!/usr/bin/python3
'''
This is the '3-my_safe_filter_states' module.

3-my_safe_filter_states uses MySQLdb to access a database (passed as argv[3])
filters for table.name to match argv[4] and prints the results.

'''
import MySQLdb
import sys
# import re

try:
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    state_name = ""
    for character in sys.argv[4]:
        if character is ';':
            break
        state_name += character
    # state_name = re.sub(r'\W+', '', state_name)
    query = "SELECT * FROM states\
     WHERE name LIKE '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

except Exception as e:
    print("No injection without protection.")
