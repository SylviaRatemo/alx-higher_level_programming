#!/usr/bin/python3
"""Lists all states with N*"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    value = argv[4]
    sql = """
    SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"""
    cursor.execute(sql, (value,))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
