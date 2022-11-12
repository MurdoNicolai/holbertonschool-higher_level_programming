#!/usr/bin/python3
"""
lists all states starting with N from the database hbtn_0e_0_usa.
arguments:
    mysql username (string)
    mysql password (string)
    database name (string)
"""


import sys
import MySQLdb


def main():
    """ Does the entire script when not imported"""

    """get information needed"""
    Username = sys.argv[1]
    Password = sys.argv[2]
    DBname = sys.argv[3]
    Host = 'localhost'

    """make connection to database"""
    database = MySQLdb.connect(Host, Username, Password, DBname)

    """cursor has simplifed modules"""
    cursor = database.cursor()

    """use database to print states"""
    cursor.execute("SELECT * FROM states Order by id")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(f"({state[0]}, '{state[1]}')")


if __name__ == '__main__':
    main()
