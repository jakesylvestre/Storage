import sqlite3
import os

conn = sqlite3.connect('database.db')#intalizing db
c = conn.cursor()

# If we are not given a path to list, use /tmp
root='/'
excludes = '/Applications'
for dir_name, sub_dirs, files in os.walk(root): #dir_name is the current directory, sub_dirs are subs and files....
    #print '\n', dir_name
    # Make the subdirectory names stand out with /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = files  #originally sub_dirs + files
    contents.sort()
    for f in contents:
        if f in excludes:#check if this directory shouldn't be walked
            continue
        print f + " is in " + dir_name
        fpath = dir_name + '/' + f
        c.execute("SELECT * FROM clusters WHERE contents = ?", (fpath,))
        #c.execute('SELECT * FROM clusters WHERE contents = '+ path);
        clustery = c.fetchone()
        if clustery is None:
            cluster = "undefined"
        else:
            cluster = clustery[0]
        cluster = "undefined" #if undefined alex will find it
        at=os.path.getatime(os.path.join(dir_name, f))#last access time of file
        c.execute('INSERT INTO scan (fpath, accessDate, cluster) VALUES (?,?,?)', (fpath,at, cluster,))#put something that is not retarted here'''
print "complete"
