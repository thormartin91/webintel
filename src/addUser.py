genres = ['unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
readNextUserIdFrom = "../data/u.info"
addUserTo = "../data/database.users"
readSentimentsFrom = "../data/database.sentiments"
addRatingTo = "../data/database.ratings"
readMovieItemsFrom = "../data/u.item"

def incrementTotalUsers(new_total):
	file = open(readNextUserIdFrom, "r")
	lines = file.readlines()
	file.close()
	lines[0] = str(new_total) + " users\n"
	file = open(readNextUserIdFrom, "w")
	for line in lines:
		file.write(line)
	file.close()

def getNewUserId():
	file = open(readNextUserIdFrom, "r")
	next_id = str(int(file.readline().split()[0])+1)            #get first word of first line of u.info, which contains amount of users. Increment and return as string
	incrementTotalUsers(next_id)
	file.close()
	return next_id

def addToUsers(line):
	users = open(addUserTo, "a")
	users.write("\n" + line)
	users.close()

def addSentimentUser():
	file_r = open(readSentimentsFrom, "r")
	lines = file_r.readlines()					#Format: movie_url | title | review | sentiment_score | rating
	file_r.close()								
	file_w = open(addRatingTo, "a")				#Format: user_id | movie_id | rating | timestamp
	for line in lines:
		temp_list = line.split('|')
		movie_info = getMovieInfo(temp_list[1])
		movie_id = movie_info[0]
		genre = movie_info[1]
		user_id = getNewUserId()
		rating = temp_list[4].strip()
		file_w.write('\n'+user_id + '|' + movie_id + '|' + rating + '|timestamp')
		addToUsers(user_id + "|age|G|Occupation|88888|"+ genre)
	file_w.close()

def getMovieInfo(title):
	movie_id = ''
	file = open(readMovieItemsFrom, encoding = "ISO-8859-1")		#Format: movie_id | title | data | url | bitstring of genres it is
	lines = file.readlines()
	id_and_genre = []
	for line in lines:
		temp_list = line.split("|")
		if title in temp_list[1]:
			movie_id = temp_list[0]
			genre = temp_list[5]
			break
		else:
			movie_id = "error"
	id_and_genre = [movie_id,genre]
	return id_and_genre

"""










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

doit()"""