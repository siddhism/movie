Movie API

An API interface to search and find movies by names, directors and genres.

It uses data from imdb.json

## Setting up project and initializing data
```
# create a virtualenv 
virtualenv env_movie
source env_movie/bin/activate
pip install -r reuqirements.txt
./manage.py migrate
./manage.py runserver 7001
./manage.py populate_movies
```


API request examples

base API url
https://pure-fortress-93926.herokuapp.com/api/movies

filter by name (full text search)
https://pure-fortress-93926.herokuapp.com/api/movies?name=wizard

filter by movie name and director name
https://pure-fortress-93926.herokuapp.com/api/movies?name=wizard&director=victor

filter by genre name
https://pure-fortress-93926.herokuapp.com/api/movies?genre=family
