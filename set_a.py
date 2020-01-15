#!/usr/bin/env python3
#
# pp. 163, 165, 166
#
from functions import *
"""
5.1 Write a program to read the 'rainfall.txt' file and the write out a
new file called 'rainfallfmt.txt'. The new file should format each
line so that the city is right-justifiled in a field that is 25
characters wide, and the rainfall data should be printed in a a field
that is 5 characters wide with 1 digit to the right of the decimal
point.
"""
rainfall = open('rainfall.txt','r')
rainfallfmt = open('rainfallfmt.txt', 'w')

for line in rainfall:
    values = line.split()
    city = values[0]
    inches = float(values[1])

    format = "%+20s %5.1f" % (city, inches)
    rainfallfmt.write(format)
    rainfallfmt.write('\n')

rainfall.close()
rainfallfmt.close()

"""
5.2 Write a function that writes a temperature coversion table called
'tempcov.txt'. The table should include temperatures from -300 to 212
degrees Fahrenheit and their Celcius equivalents, presented in two
columns with appropriate headings. Each collumn should be 10
characters wide, and each temperature should have 3 digits to the
right of the decimal point.
"""

def tempconvert():
    tempcov = open('tempcov.txt', 'w')
    for i in range(513):
        Cel = (i - 300)
        Fah = ((i - 300) * 9/5 + 32)
        tempcov.write("% +10s %+3s %5.1f %+3s" % (Cel, "Celcius",  Fah, "Fahrenheit"))
        tempcov.write('\n')

tempconvert()
"""
5.3 Open a file during a Pyhton session. Call the 'readline' method twice
on that file, then call the 'readlines' method. What lines does the
list reurned by 'readlines' include?
"""

#readline prints a speciied number o characters, or if not specified, the whole
#line, automatically advances to next line

#readlines reads the whole file in plain text, not interpreting newline
#characters

"""
5.4 Open the file in Exercise 5.3 again, but call 'readlines'
immediately. Compare the lines returned in this excercise with the
previous one.
"""
#reads the whole file instead of just all the remaining lines


"""
5.5 Write a program that reads in the contents of a file and writes a new
file where all the characters are in uppercase.
"""

upperfile = open('upperCaseFile.txt', 'w')
upperfile.write(returnUpercase('rickastley.txt'))
upperfile.close()

"""
5.6 Write a program that reads in a file and then prints out the number
of lines, words, and characters in the file.
"""



"""
5.7 Write a program that creates a file with a concordance - an index
that tells you the line of the file wach word appears on. If a word
is on more tha one line, the concordance will show you all of the
lines containing that word. Hint: Use a dictionary keyed by each word
to solve this problem.
"""

lyrics = open('rickastley.txt', 'r')
word_dict = {}
line_num = 1
for line in lyrics:
    words = line.split()
    for word in words:
        word = word.lower()
        word = word.strip()
        for char in [',','.','?','(',')']:
            word = word.replace(char,'')
        if word in word_dict:
            if line_num not in word_dict[word]:
                word_dict[word].append(line_num)
        else:
            word_dict[word] = [line_num]
    line_num = line_num + 1
output = open('word_dict.txt', 'w')
output.write(str(word_dict))
output.close()
print(word_dict)
