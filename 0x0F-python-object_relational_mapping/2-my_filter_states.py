#!/usr/bin/python3
"""displays all values in the states table where name matches the argument"""


def main():
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         password=password, db=dbname)
    cursor = db.cursor()
    query = f"SELECT * FROM states WHERE name = '{name}' ORDER BY states.id;"
    cursor.execute(query)
    result = cursor.fetchall()
    for item in result:
        print(item)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
