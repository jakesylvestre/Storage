import sqllite
import os

conn = sqlite3.connect('database.db')#intalizing db
c = conn.cursor()

# If we are not given a path to list, use /tmp
root='/'
for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
    #print '\n', dir_name
    # Make the subdirectory names stand out with /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = files  #originally sub_dirs + files
    contents.sort()
    for f in contents:
        print f + " is in " + dir_name
        
        c.execute('INSERT INTO scan (' + f, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);')#put something that's not retarted here

'''
I'm tired and have to go to bed, here's what you need to know, first look at alex's dbsetup.py file
it should have everything you need, insert right shit into right problems, last access is a different story, ask this is irc:
 hey guys, does anyone know how I can access last modification of the files and not their paths, similiar to this: os.path.getatime(path

talk to alex about fpath., other than that you should be fine

'''
