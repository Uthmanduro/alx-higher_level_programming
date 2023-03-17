#!/usr/bin/python3
""" lists all cities of a state using the database"""


import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON\
                cities.state_id = states.id WHERE states.name = %s\
                ORDER BY cities.id;", (sys.argv[4],))
    cities = cur.fetchall()
    for i, items in enumerate(cities):
        if i == len(cities) - 1:
            print(''.join(items))
        else:
            print(f"{''.join(items)}, ", end="")
    cur.close()
    db.close()
