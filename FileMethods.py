'''
    File Methods with examples
'''

''' Reading from a file''' 
file = open('FileMethods.txt', 'r')

lineList = []
print("Output from reading the file")
for line in file:

    print(line, end = "")
    lineList.append(line)

file.close()

#####################################################################################
''' Appending data to a file. '''
file = open('FileMethods.txt', 'a')

wordList = ['Oranges\n', 'Peacock\n', 'Waterfall\n']
for i in wordList:

    file.write(i)

file.close()
# output the appended values by reading from file
file = open('FileMethods.txt', 'r')
for i in file:
    
    print(i, end = "")
file.close()

######################################################################################

''' Writing data to a file. '''

file = open('FileMethods.txt', 'w')

wordList = ['Expelliarmus\n', 'Severus Snape\n', 'Dumbledore\n', 
                        'Potter\n', 'Patronous\n', 'Sectumsempra\n']
string = ''
for word in wordList:

    string += word

file.write(string)
file.close()

file = open('FileMethods.txt', 'r')
for i in file:
    
    print(i, end = "")
file.close()
