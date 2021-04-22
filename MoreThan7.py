'''
    Write a function words() in python to read lines from a text file "WORD.txt", 
    and display those words, which are less than 7 characters.
'''

if __name__ == "__main__":

    file = open("Q4.txt", 'r')
    count = 0
    for i in file:

        for word in i.split():

            if len(word) < 7:

                count += 1
    print(count)