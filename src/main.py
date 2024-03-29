import addUser
'''
Global variables, loaded through loadData()
  users:
    { 'user_id': { 'genres': genres_string } }
  movies:
    { 'movie_id': { 'title': movie_title, 'genres': genres_string } }
  user_ratings:
    { 'user_id': { 'movie_title': rating } }
  movie_ratings:
    { 'movie_title': { 'user_id': rating } }
'''
genres = addUser.genres
users = {}
movies = {}
user_ratings = {}
movie_ratings = {}

def prettyPrint(dictionary):
  '''
  Returns an indented string of the supplied dictionary
  '''
  import json
  return json.dumps(dictionary, sort_keys=True, indent=4)


def loadData(path='../data'):
  '''
  Loads data into global variables
  '''
  # Load movies
  for line in open(path+'/u.item',encoding = "ISO-8859-1"):
    (movie_id, title, release_date, video_date, imdb) = line.split('|')[0:5]
    movies.setdefault(movie_id,{})
    movies[movie_id]['title'] = title
    genres_string = ''.join(line.split('|')[5:24]).replace('\n', '')
    movies[movie_id]['genres'] = genres_string
    #print movie_id,title,release_date,video_date,imdb,genres_string

  # Load users
  for line in open(path+'/database.users'):
    (user_id, age, gender, occupation, postal_code, genres_string) = line.split('|')
    users.setdefault(user_id,{})
    users[user_id]['genres'] = genres_string.replace('\n', '')
    #print user_id, age, gender, occupation, postal_code, genres_string
  
  # Load user_ratings
  for line in open(path+'/database.ratings'):
    (user_id,movie_id,rating,timestamp) = line.split('\t')
    user_ratings.setdefault(user_id,{})
    user_ratings[user_id][movies[movie_id]['title']] = float(rating)
    #print user_id,movie_id,rating,timestamp

  # Load movie_ratings (flipping the user_ratings)
  for user in user_ratings:
    for movie in user_ratings[user]:
      movie_ratings.setdefault(movie, {})
      movie_ratings[movie][user] = user_ratings[user][movie]

  return True


# Load data from sample
#loadData(path='../sample')
loadData()
#print 'USERS', prettyPrint(users), '\n'
#print 'MOVIES', prettyPrint(movies), '\n'
#print 'USER_RATINGS', prettyPrint(user_ratings), '\n'
#print 'MOVIE_RATINGS', prettyPrint(movie_ratings), '\n'


def topGenre(user_id):
  '''
  Returns a list of top 10 movie titles within all genres selected by user
  DEPRECATED:
    # Returns a dictionary of the users prefered genres with sorted list of top rated movies
    # top_list = { 'genre': [(average_rating, movie_title), ...] }
  '''
  loadData()
  user_genre = users[user_id]['genres']
  #top_dict = {}
  top_list = []
  for movie in movies:
    title = movies[movie]['title']
    if title not in movie_ratings: continue # skip movie if it has no rating
    for index,value in enumerate(user_genre): # loop trough users genres
      if value == '1': # user prefers this genre
        if movies[movie]['genres'][index] == '1': # this movie is in this genre
          #top_dict.setdefault(genres[index], [])
          average_rating = round(sum(movie_ratings[title].values())/len(movie_ratings[title]), 3)
          #top_dict[genres[index]].append((average_rating, title))
          top_list.append((average_rating,title))
  # sort each list with decending rating
  #for movie_list in top_dict:
  #  top_dict[movie_list].sort()
  #  top_dict[movie_list].reverse()
  top_list = list(set(top_list)) # remove duplicates
  top_list.sort(reverse=True)
  top_list_clean = []
  [top_list_clean.append(item[1]) for item in top_list[:10]] 
  return top_list_clean


def pearson(x, y):
  '''
  Returns the similarity between two objects
  HACK:
    - ceiling of average due to cold start only accepting top score..
  '''
  from math import sqrt, ceil
  shared_movies = []
  for movie in user_ratings.get(x,{}):
    if movie in user_ratings.get(y,{}):
      shared_movies.append(movie)
  n =len(shared_movies)
  if n == 0: return 0
  mean_x = sum(ceil(user_ratings[x][movie]) for movie in shared_movies)/n
  mean_y = sum(ceil(user_ratings[y][movie]) for movie in shared_movies)/n
  numerator,denominator = 0,0
  for movie in shared_movies:
    numerator += ((user_ratings[x][movie] - mean_x) * (user_ratings[y][movie] - mean_y))
    denominator += (sqrt(pow((user_ratings[x][movie] - mean_x),2)) * sqrt(pow((user_ratings[y][movie] - mean_y),2)))
  if denominator == 0: return 0
  return numerator/denominator


def findMovies(this_user):
  '''
  Returns a list of top 10 movie titles reccommended movies for the given user
  DEPRECATED:
    # Returns an ordered list of reccommended movies for the given user
      # [(calculated_ranking, movie_title), ...]
  '''
  loadData()
  flip = {1:5, 2:4, 3:3, 4:2, 5:1}
  total_similarities = {} # {movie: (rating * similarity)} for all similar users (and shared movies)
  sum_of_similarities = {} # {movie: similarity} for all similar users (and shared movies)
  for user in user_ratings:
    if user == this_user: continue # skip this_user
    similarity = pearson(this_user, user) # compute similarity
    if similarity == 0: continue # ignore un-simmilar users
    for movie in user_ratings[user]:
      if movie not in user_ratings[this_user]: # if movie not seen by this_user
        if similarity <= 0: # negative correlation, flip rating and similarity
          rating = flip[user_ratings[user][movie]]
          similarity = abs(similarity)
        total_similarities.setdefault(movie, 0)
        total_similarities[movie] += (user_ratings[user][movie] * similarity)
        sum_of_similarities.setdefault(movie, 0)
        sum_of_similarities[movie] += similarity
  # compute calculated ranking for this_user
  # sum(rating * similarity) / sum(similarity) for all users sharing the movie
  rankings = [(round(total/sum_of_similarities[item],3),item) for item,total in total_similarities.items()]
  rankings.sort(reverse=True)
  rankings_clean = []
  [rankings_clean.append(item[1]) for item in rankings[:10]] 
  return rankings_clean
