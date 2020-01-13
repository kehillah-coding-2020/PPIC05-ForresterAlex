def returnUpercase(file):
    file = open(file, 'r')
    filecontent = ''
    for lines in file:
        filecontent = filecontent + file.readline()
    filecontentupper = filecontent.upper()
    return filecontentupper
