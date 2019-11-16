import requests
from bs4 import BeautifulSoup
import json


def preprocess (url):
    response = requests.get(url, timeout=10)
    content = BeautifulSoup(response.content, 'html.parser')
    for movie in content.find_all('div', attrs={'class': 'lister-item-content'}):
        name = movie.find('a').get_text()
        rating = movie.find('strong').get_text()
        date = movie.find('span', attrs={'class': 'lister-item-year text-muted unbold'}).get_text()
        movie_names.append(name)
        movie_year.append(date)
        movie_imdbrating.append(rating)
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

genre_to_url = {
    'action': 'https://www.imdb.com/search/title/?genres=action&sort=num_votes,desc&explore=title_type,genres',
    'adventure': 'https://www.imdb.com/search/title/?genres=adventure&sort=num_votes,desc&explore=title_type,genres',
    'animation': 'https://www.imdb.com/search/title/?genres=animation&sort=num_votes,desc&explore=title_type,genres',
    'biography': 'https://www.imdb.com/search/title/?genres=biography&sort=num_votes,desc&explore=title_type,genres',
    'comedy': 'https://www.imdb.com/search/title/?genres=comedy&sort=num_votes,desc&explore=title_type,genres',
    'crime': 'https://www.imdb.com/search/title/?genres=crime&sort=num_votes,desc&explore=title_type,genres',
    'documentary': 'https://www.imdb.com/search/title/?genres=documentary&sort=num_votes,desc&explore=title_type,genres',
    'drama': 'https://www.imdb.com/search/title/?genres=drama&sort=num_votes,desc&explore=title_type,genres',
    'family': 'https://www.imdb.com/search/title/?genres=family&sort=num_votes,desc&explore=title_type,genres',
    'fantasy': 'https://www.imdb.com/search/title/?genres=fantasy&sort=num_votes,desc&explore=title_type,genres',
    'film-noir': 'https://www.imdb.com/search/title/?genres=film-noir&sort=num_votes,desc&explore=title_type,genres',
    'history': 'https://www.imdb.com/search/title/?genres=history&sort=num_votes,desc&explore=title_type,genres',
    'horror': 'https://www.imdb.com/search/title/?genres=horror&sort=num_votes,desc&explore=title_type,genres',
    'music': 'https://www.imdb.com/search/title/?genres=music&sort=num_votes,desc&explore=title_type,genres',
    'musical': 'https://www.imdb.com/search/title/?genres=musical&sort=num_votes,desc&explore=title_type,genres',
    'mystery': 'https://www.imdb.com/search/title/?genres=mystery&sort=num_votes,desc&explore=title_type,genres',
    'romance': 'https://www.imdb.com/search/title/?genres=romance&sort=num_votes,desc&explore=title_type,genres',
    'sci-fi': 'https://www.imdb.com/search/title/?genres=sci-fi&sort=num_votes,desc&explore=title_type,genres',
    'sport': 'https://www.imdb.com/search/title/?genres=sport&sort=num_votes,desc&explore=title_type,genres',
    'thriller': 'https://www.imdb.com/search/title/?genres=thriller&sort=num_votes,desc&explore=title_type,genres',
    'war': 'https://www.imdb.com/search/title/?genres=war&sort=num_votes,desc&explore=title_type,genres',
    'western': 'https://www.imdb.com/search/title/?genres=western&sort=num_votes,desc&explore=title_type,genres',
}
genre = input('Enter your genre ').lower()
preprocess(genre_to_url[genre])


with open('imdb.json', 'w') as output:
    json.dump(movies, output)






