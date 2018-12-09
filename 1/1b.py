fileLines = open("input.txt", "r")
allLine = fileLines.readlines()
hitFreq = set()

freq = 0
firstDoubleFreq = 0
runloop = True

while runloop:
    for line in allLine:
        
        freq = freq + int(line)
        print(freq)
        if  freq in hitFreq:
            firstDoubleFreq = freq
            runloop = False
            break
        else:    
            hitFreq.add(freq)

print(freq)
