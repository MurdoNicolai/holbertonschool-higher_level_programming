#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_0_usa that are in given state.
arguments:
    mysql username (string)
    mysql password (string)
    database name (string)
    state name (string)
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
    state_name = sys.argv[4]

    """make connection to database"""
    database = MySQLdb.connect(Host, Username, Password, DBname)

    """cursor has simplifed modules"""
    cursor = database.cursor()

    """use database to print states"""
    cursor.execute("SELECT * FROM states s\
                    RIGHT JOIN cities c \
                    ON s.id = c.state_id")
    cities = cursor.fetchall()
    first_print = 1
    for citie in cities:
        if citie[1] == state_name:
            if first_print == 0:
                print("", end=", ")
            else:
                first_print = 0
            print(f"{citie[4]}", end='')
    print()


if __name__ == '__main__':
    main()
