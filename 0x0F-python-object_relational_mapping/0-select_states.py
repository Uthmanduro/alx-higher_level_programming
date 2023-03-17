#!/usr/bin/python3
"""lists al states from the database"""
def main():
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, database=dbname)
    cur = db.cursor()
    with open('0-select_states.sql', 'r') as filename:
        my_script = filename.read()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    table = cur.fetchall()
    for item in table:
        print(item)
    cur.close()
    db.close()
if __name__ == '__main__':
    main()
