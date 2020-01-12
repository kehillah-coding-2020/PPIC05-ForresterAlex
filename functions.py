def returnUpercase(file):
    file = open(file, 'r')
    upperCaseFile = open('upperCase_' + file, 'w')
    filecontent = file.readlines()
    filecontentupper = filecontent.upper()
    upperCaseFile.write(filecontentupper)
