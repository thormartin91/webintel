ratings_file = '../data/database.ratings'
info_file = '../data/u.info'


def addRating(movie_id, user_id, rating):
	'''
	Adds given ratings to file, and updates total ratings number
	'''
	import time
	timestamp = int(time.time())
	line = str(user_id) + '\t' + str(movie_id) + '\t' + str(rating) + '\t' + str(timestamp)
	addToRatingsFile(line)
	incrementTotalRatings()


def addToRatingsFile(line):
	ratings = open(ratings_file, "a")
	ratings.write("\n" + line)
	ratings.close()

def incrementTotalRatings():
	file = open(info_file, "r")
	lines = file.readlines()
	file.close()
	ratings = int(lines.pop().split(' ')[0])
	ratings += 1
	lines.append(str(ratings) + ' ratings')
	file = open(info_file, "w")
	for line in lines:
		file.write(line)
	file.close()
