fileLines = open("input.txt", "r")


freq = 0
for line in fileLines:
    print (line)
    freq = freq + int(line)

print(freq)






