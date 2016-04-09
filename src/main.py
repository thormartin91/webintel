'''
Global variables, loaded through loadData()
  movies:
    { 'movie_id': 'movie_title' }
  user_ratings:
    { 'user_id': { 'movie_title': rating } }
  movie_ratings:
    { 'movie_title': { 'user_id': rating } }
'''
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
  for line in open(path+'/u.item'):
    (id, title, release_date, video_date, imdb) = line.split('|')[0:5]
    movies[id] = title
    genres_string = ''.join(line.split('|')[5:24]).replace('\n', '')
  
  # Load user_ratings
  for line in open(path+'/u.data'):
    (user_id,movie_id,rating,timestamp) = line.split('\t')
    user_ratings.setdefault(user_id,{})
    user_ratings[user_id][movies[movie_id]] = float(rating)

  # Load movie_ratings (flipping the user_ratings)
  for user in user_ratings:
    for movie in user_ratings[user]:
      movie_ratings.setdefault(movie, {})
      movie_ratings[movie][user] = user_ratings[user][movie]

  return True


# Load data from sample
#loadData(path='../sample')
loadData()
#print 'MOVIES', prettyPrint(movies), '\n'
#print 'USER_RATINGS', prettyPrint(user_ratings), '\n'
#print 'MOVIE_RATINGS', prettyPrint(movie_ratings), '\n'


def pearson(x, y):
  '''
  Returns the similarity between two objects
  '''
  from math import sqrt
  shared_movies = []
  for movie in user_ratings[x]:
    if movie in user_ratings[y]:
      shared_movies.append(movie)
  n =len(shared_movies)
  if n == 0: return 0
  mean_x = sum(user_ratings[x][movie] for movie in shared_movies)/n
  mean_y = sum(user_ratings[y][movie] for movie in shared_movies)/n
  numerator,denominator = 0,0
  for movie in shared_movies:
    numerator += ((user_ratings[x][movie] - mean_x) * (user_ratings[y][movie] - mean_y))
    denominator += (sqrt(pow((user_ratings[x][movie] - mean_x),2)) * sqrt(pow((user_ratings[y][movie] - mean_y),2)))
  if denominator == 0: return 0
  return numerator/denominator


def findMovies(this_user):
  '''
  Returns an ordered list of reccommended movies for the given user
    [(calculated_ranking, movie_title), ...]
  TODO:
    - What about negative corelation?
      (ignore users with a negative corelation for now)
  '''
  total_similarities = {} # {movie: (rating * similarity)} for all similar users (and shared movies)
  sum_of_similarities = {} # {movie: similarity} for all similar users (and shared movies)
  for user in user_ratings:
    if user == this_user: continue # skip this_user
    similarity = pearson(this_user, user) # compute similarity
    if similarity <= 0: continue # ignore un-simmilar users
    for movie in user_ratings[user]:
      if movie not in user_ratings[this_user]: # if movie not seen by this_user
        total_similarities.setdefault(movie, 0)
        total_similarities[movie] += (user_ratings[user][movie] * similarity)
        sum_of_similarities.setdefault(movie, 0)
        sum_of_similarities[movie] += similarity
  # compute calculated ranking for this_user
  # sum(rating * similarity) / sum(similarity) for all users sharing the movie
  rankings = [(round(total/sum_of_similarities[item],3),item) for item,total in total_similarities.items()]
  rankings.sort()
  rankings.reverse()
  return rankings


rec = findMovies('1')
for r in rec:
  print r