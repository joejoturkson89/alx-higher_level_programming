#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

def main(args):

    if len(args) != 4:
        raise Exception("need 3 arguments!")
    db = MySQLdb.connect(host='localhost',
            user=args[1],
            passwd=args[2],
            db=args[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    states = c.fecthall()
    for state in states:
        print(state)

if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
