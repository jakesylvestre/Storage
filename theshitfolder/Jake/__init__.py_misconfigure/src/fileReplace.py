import __init__

def fileReplace(path):
    os.remove(path)
    newPath = path + ".ctx"
    file = open(newpath, 'w+')
