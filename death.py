loopfile = open("loopfile.txt", 'r+')
loopfile.write("Ω")
for i in range(9999999999999999999999):
    loopfile.write("Ω" * i)
    loopfile.write('\n')
