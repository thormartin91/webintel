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
loadData(path='../sample')
print prettyPrint(movies)
print prettyPrint(user_ratings)
print prettyPrint(movie_ratings)


def pearson(object_1, object_2):
  from random import random
  '''
  Returns the similarity between two objects
  '''
  # TODO: implement this
  return round(random(),1)


def findMovies(this_user):
  '''
  Returns an ordered list of reccommended movies for the given user
  TODO:
    - How many similar users should we look at?
      (Only looking at the most simmilar, for now)
    - What is the criteria for ordering movies rated by the simmilar user?
      (The highest rated movie of the simmilar user comes first, for now)
  '''
  other_users = {} # 'other_user_id': similarity_score
  for movie in user_ratings[this_user]: # movies this_user has rated
    for user in movie_ratings[movie]: # users who also has rated this movie
      if user != this_user: # do not compare with self
        other_users[user] = pearson(this_user, user) # compute similarity
  similar_users = sorted(other_users, key=other_users.get, reverse=True) # sorted list of IDs for the most simmilar users
  movies = user_ratings[similar_users[0]] # find movies rated by the most similar user
  reccommended_movies = sorted(movies, key=movies.get, reverse=True) # sorted list of IDs for the highest rated movies users of the most simmilar user
  return reccommended_movies


#print findMovies('1')
