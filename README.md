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

Admin url
access : http://abc.herokuapp.com/admin/
username : siddhesh
password : fynd1234

API request examples

base API url
http://localhost:7000/api/movies

filter by name (full text search)
http://localhost:7000/api/movies?name=wizard

filter by movie name and director name
http://localhost:7000/api/movies?name=wizard&director=victor

filter by genre name
http://localhost:7000/api/movies?genre=family
