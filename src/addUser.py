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
	return next_id


def addToUsers(line):
	users = open(addUserTo, "a")
	users.write("\n" + line)

def promptForGenrePrefs():
	binaryString = "0"												#Sets "unknown" genre to 0 by default
	for i in range(1, len(genres)):
		pref = raw_input("Do you like " + genres[i] + "? (Y/N) ").upper()
		if pref == "Y":
			binaryString += "1"
		else:
			binaryString += "0"
	return binaryString

registerUser()

#todo
#inkrementere users i info