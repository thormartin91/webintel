import unirest

def getSentiment(text):
	response = unirest.post("https://japerk-text-processing.p.mashape.com/sentiment/", 
		headers = {
			"X-Mashape-Key": "FaN6UDxp88mshuIwEw8rKDks8og0p1Hjqx3jsnbtNuuIcjZakF",
			"Content-TYpe": "application/x-www-form-urlencoded",
			"Accept": "application/json"
		},
		params = {
			"language": "english",
			"text": text
		}
	)


	return response.body["probability"]

def mainFunction(filename="seventhTest.txt", outputFile="output.txt"):
	oldFile = open(filename, "r")
	newFile = open(outputFile, "a")
	newString = ""
	lineList = []
	start = 1256
	stop = start
	increase = 25
	for line in oldFile:
		lineList.append(line)
	end = len(lineList)
	while stop < end:
		if (start + increase < len(lineList)):
			stop += increase
		else:
			stop = len(lineList)
		print("Started processing: ", str(start), " to: ", str(stop), "\n")
		for l in lineList[start:stop]:
			splitLine = l.split("|")
			newString = splitLine[0] + "|" + splitLine[1] + "|" + splitLine[2]
			try:
				responseBody = getSentiment(splitLine[2])
				print(responseBody)
				for key in responseBody:
					newString += "|" + str(responseBody[key])
			except:
				print("Error occured")
				newString += "|0|0|0"
			#print(newString)
			newFile.write(newString + "\n")
		start = stop
	oldFile.close()
	newFile.close()

def setGrades(filename="sentiment.txt", outputFile="output.txt"):
	oldFile = open(filename, "r")
	newFile = open(outputFile, "w")
	newLines = []
	grades = []
	for line in oldFile:
		newLines.append(line)
	for l in newLines:
		l = l.strip()
		splitLine = l.split("|")
		grade = weighSentiments(float(splitLine[3]), float(splitLine[4]), float(splitLine[5]))
		grades.append(grade)
		newFile.write(l + "|" + str(grade) + "\n")
	gradeStats(grades)

def gradeStats(grades):
	gradeStats = [0, 0, 0, 0, 0]
	for grade in grades:
		gradeStats[grade-1] += 1
	print gradeStats

def weighSentiments(neg, neut, pos):
	limits = [-0.5, 0, 0.5]
	neutLimits = [0.25, 0.75]
	posMinusNeg = pos - neg
	possibleGrades =  [0, 0]
	grade = 0
	# p - n < -0.5
	if (posMinusNeg < limits[0]):
		if (neut > neutLimits[1]):
			grade = 2
		else:
			grade = 1
	# -0.5 < p - n < 0
	elif (posMinusNeg < limits[1]):
		if (neut > neutLimits[0]):
			grade = 3
		else:
			grade = 2
	# 0 < p - n < 0.5
	elif (posMinusNeg < limits[2]):
		if (neut > neutLimits[0]):
			grade = 3
		else:
			grade = 4
	# 0.5 < p - n
	else:
		if (neut > neutLimits[1]):
			grade = 4
		else:
			grade = 5
	return grade


setGrades()







