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
    SELECT t1.name
    FROM cities t1
    LEFT JOIN states t2 ON t1.state_id = t2.id WHERE t2.name = %s ORDER BY t1.id ASC;"""
    cursor.execute(sql, (value,))
    query_rows = [row[0] for row in cursor.fetchall()]
    print(", ".join(query_rows), end='\n')
    cursor.close()
    connection.close()
