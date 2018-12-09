from collections import Counter
fileLines = open("input.txt", "r")
allLine = fileLines.readlines()

occuredTwice = 0
OccuredTrice = 0

for line in allLine:
    contains2 = False
    contains3 = False
    count = Counter(line)
    for value in count:
        if count[value] is 2 :
            contains2 = True
        if count[value] is 3 :
            contains3 = True

    if contains2 :
        occuredTwice += 1
    if contains3:
        OccuredTrice += 1

print(occuredTwice * OccuredTrice)
