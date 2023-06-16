#!/usr/bin/python3
"""Lists all states with N*"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    sql = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql)
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cursor.close()
    connection.close()
