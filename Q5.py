file = open('Q5.txt', 'r')
count = 0
for i in file:

    for word in i.split():

        if word == 'is':
            count += 1
print(count)
file.close()
