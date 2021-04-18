'''
    Write a function in python to count the number of lines from a text file "WORD.txt" which is not starting with an alphabet "S".
    Example: If the file "story.txt" contains the following lines: A boy is playing there.
    She is good.
    An aeroplane is in the sky.
    sky is pink.
    Alphabets and numbers are allowed in the password.
    Output: No of lines not starting with 'S'= 2
'''

if __name__ == "__main__":

    file = open("Q3.txt", 'r')
    lines = file.readlines()
    count = 0
    for i in lines:

        if i[0] == 'S':
            count += 1
    
    print(count)
