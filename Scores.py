''' 
    You are given a file called class_scores.txt, where each line of the file contains a oneword
    username and a test score separated by spaces, like below:
    nagateja 92
    anuhta 93
    Write code that scans through the file, adds 6 points to each test score, and outputs the usernames
    and new test scores to a new file, scores2.txt.
'''

if __name__ == "__main__":


    file = open("class_scores.txt", 'r')
    string = ""
    for i in file:

        name, score = i.split()
        score = int(score)
        score = score + 6
        score = str(score)

        string += name + " " + score + "\n"
        
    file.close()
    file = open("scores2.txt", 'w')
    file.write(string)
    file.close()

        
            