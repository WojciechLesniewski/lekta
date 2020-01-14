#!/usr/bin/env python
import sys
import request
from time import sleep
import psycopg2
try:
    conn = psycopg2.connect("dbname='db' user='postgres' host='localhost' password='postgres'")
    print 'Connected to db'
except:
    print 'I am unable to connect to the database' 
    sys.exit(1)

def main():
    cur = conn.cursor()
    cur.execute('ALTER TABLE events ADD COLUMN IF NOT EXISTS ip_address varchar(255) NOT NULL DEFAULT 1;')
    conn.commit()

if __name__ == '__main__':
    main()
