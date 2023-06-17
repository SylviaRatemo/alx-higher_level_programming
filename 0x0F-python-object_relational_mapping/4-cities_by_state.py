#!/usr/bin/python3
"""Lists all states with N*"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()

    sql = """
    SELECT t1.id, t2.name, t1.name
    FROM cities t1
    JOIN states t2 ON t1.state_id = t2.id ORDER BY t1.id ASC"""
    cursor.execute(sql)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
