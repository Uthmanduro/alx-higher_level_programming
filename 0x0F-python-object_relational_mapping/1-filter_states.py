#!/usr/bin/python3
"""lists all states with a name starting with 'N' from the database"""


def main():
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, database=dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                   COLLATE utf8mb4_general_ci ORDER BY states.id ASC;")
    result = cursor.fetchall()
    for item in result:
        print(item)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
