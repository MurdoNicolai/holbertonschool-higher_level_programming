#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa.
arguments:
    mysql username (string)
    mysql password (string)
    database name (string)
"""


import sys
import MySQLdb


def main():
    """ Does the entire script when not imported"""

    #get information needed
    Username = sys.argv[1]
    Password = sys.argv[2]
    DBname = sys.argv[3]
    Host = 'localhost'

    #make connection to database
    database = MySQLdb.connect(host=Host, user=Username, passwd=Password, db=DBname)

    #cursor has simplifed modules
    cursor = database.cursor()

    #use database to print states
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        print (f"({state[0]}, '{state[1]}')")

if __name__ == '__main__':
    main()
