'''
Creates database and subsequent tables on users computer
'''
import sqlite3
conn = sqlite3.connect('database.db')#intalizing db
c = conn.cursor()
#setting up all of the tables

#test for fileMap
try:
    c.execute(''' SELECT * FROM  fileMap''')#whaqt the fuck is a file map
except sqlite3.OperationalError:
#files
    c.execute('''CREATE TABLE fileMap(fpath text, size text)''')
try:
    c.execute(''' SELECT * FROM  scan''')
except sqlite3.OperationalError:
#files
    c.execute('''CREATE TABLE scan(fpath text, accessDate text)''')
