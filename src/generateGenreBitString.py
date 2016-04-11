import random
defaultReadFrom = "../data/u.user"
defaultReadTo = "../data/database.users"

def generateBitString():
    bitstring = ""
    for i in range(19):
        if (random.randint(1,3) == 1):
            bitstring += "1";
        else:
            bitstring += "0";
    return bitstring

def appendGenreBitString(readFrom, readTo):
    oldFile = open(readFrom, "r")
    newFile = open(readTo, "w")
    for line in oldFile:
        line = line.strip()
        line += "|" + generateBitString() + "\n"
        newFile.write(line)

def run():
    fileToReadFrom = raw_input("Filename to read FROM (" + defaultReadFrom + "): ")
    if (fileToReadFrom == ""):
        fileToReadFrom = defaultReadFrom
        print "shit didn't work"
    fileToReadTo = raw_input("Filename to read TO (" + defaultReadTo + "): ")
    if (fileToReadTo == ""):
        fileToReadTo = defaultReadTo
        print "shit didn't work: " + fileToReadTo
    appendGenreBitString(fileToReadFrom, fileToReadTo)

run()

        
