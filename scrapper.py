import requests
from bs4 import BeautifulSoup
import json


def preprocess (url):
    response = requests.get(url, timeout=10)
    content = BeautifulSoup(response.content, 'html.parser')
    for movie in content.find_all('td', attrs={'class': 'titleColumn'}):
        name = movie.find('a').get_text()
        date = movie.find('span', attrs={'class': 'secondaryInfo'}).get_text()
        movie_names.append(name)
        movie_year.append(date)
    for movie in content.find_all('td', attrs={'class': 'ratingColumn imdbRating'}):
        name = movie.find('strong').get_text()
        movie_imdbrating.append(name)
    sz = len(movie_names)
    for i in range(0, sz):
        data = {
            "name": movie_names[i],
            "year": movie_year[i].strip('()'),
            "rating": movie_imdbrating[i]
        }
        movies.append(data)



movie_names = []
movie_year = []
movie_imdbrating = []
movies = []


preprocess ('https://www.imdb.com/chart/top')


with open('imdb.json', 'w') as output:
    json.dump(movies, output)






