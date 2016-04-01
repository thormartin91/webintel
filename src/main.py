# Global variables, loaded through loadData()
movies = {}
ratings = {}


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
  
  # Load ratings
  for line in open(path+'/u.data'):
    (user_id,movie_id,rating,timestamp) = line.split('\t')
    ratings.setdefault(user_id,{})
    ratings[user_id][movies[movie_id]] = float(rating)
  return True


# Load data from sample
loadData(path='../sample')
