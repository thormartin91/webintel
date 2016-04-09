#genres from 0 - 18
genres = ['unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

readNextUserIdFrom = "../data/u.info"

addUserTo = "../data/u.user"

def registerUser():
    user_id = getNewUserId()
    name = raw_input("Name:")										#Name will not be registered with user
    age = raw_input("Age:")
    gender = raw_input("Gender (M/F):").upper()						#raw_input
    occupation = raw_input("Occupation:")
    zip_code = raw_input("Zip Code:")
    preferences = promptForGenrePrefs()
    
    line_to_add = str(user_id) + "|" + age + "|" + gender + "|" + occupation + "|" + zip_code + "|" + preferences
    addToUsers(line_to_add)

def getNewUserId():
	file = open(readNextUserIdFrom, "r")
	next_id = str(int(file.readline().split()[0])+1)				#get first word of first line of u.info, which contains amount of users. Increment and return as string
	file.close()
	incrementTotalUsers(next_id)
	return next_id


def addToUsers(line):
	users = open(addUserTo, "a")
	users.write("\n" + line)
	users.close()

def promptForGenrePrefs():
	binary_string = "0"												#Sets "unknown" genre to 0 by default
	for i in range(1, len(genres)):
		pref = raw_input("Do you like " + genres[i] + "? (Y/N) ").upper()
		if pref == "Y":
			binary_string += "1"
		else:
			binary_string += "0"
	return binary_string

def incrementTotalUsers(new_total):
	file = open(readNextUserIdFrom, "r")
	lines = file.readlines()
	file.close()
	print(lines)
	lines[0] = str(new_total) + " users\n"
	print(lines)
	file = open(readNextUserIdFrom, "w")
	for line in lines:
		file.write(line)
	file.close()

def doit():
	stringliste = ""
	for i in range(1,len(genres)):
		stringliste+= "var"+str(i)+".get(),"
		#h = open(addUserTo, "a")
		#h.write("\n" + genres[i].lower()+"_c = Checkbutton(state = ACTIVE, text = '"+genres[i]+"', variable = var"+str(i)+").pack()")
		#h.write("\n"+"var"+str(i)+" = IntVar()")

	h = open(addUserTo, "a")
	h.write(stringliste)
	h.close()

doit()