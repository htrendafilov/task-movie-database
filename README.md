# uIMDB Movie Database task

## Description
The task is to implement very, very, veru simplified IMDB like movie database.
It should:
  - store the movie data in a database
  - Have REST API to query, create and update movie record
  - initialize the database if empty from:  https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea
  - use whatever technology stack you prefer
  
 Full description (in Bulgarian) is in ***documents/task_definition.txt***
 
## Design Overview

I decided to do it Python (because lately I wrote mostly Python), but will give it a try with Java later.

The main components are:

![](https://raw.githubusercontent.com/htrendafilov/task-movie-database/master/documents/uIMDB_Design.png)

I decided on:
 - **Flask** as the WEB framework
 - Using **Swagger** to describe the rest API and **Connexion** to make it Pythonic
 - **SQLAlchemy** is used for ORM and **Marshmallow** for serialization/deserialization to JSON

## Files' descriptions
 - main.py - The entry point. Starts the Server.
 - models.py - include the model of the objects used. (In this case only Movie object)
 - swagger.yml - Defines the REST API
 - config.py - App configurations. In this case Database used is configured here
 - movie.py - The REST API is implemented here
 - requirements.txt - The python libraries used. Install with: `pip install -r requirements.txt`
 - initilize_database.py - One-off script to be run to initialize the DB for the first time
 - test_movie.py - Test cases, using **pytest**
 
 ## Usage
 
 Before first run, install the requirements: `pip install -r requirements.txt` and initialize the database: `python initialize_database.py`  
 Then start the app with `main.py` file.  
 The test are run with: `pytest`  
 
 The API is under: `http://localhost:5000/api/`  
 Swagger UI could be accessed on: `http://localhost:5000/api/ui`

 ## Example Queries
 
 Get all movies:
```
 $ curl -s -X GET --header 'Accept: application/json' 'http://localhost:5000/api/movie'
[
  {
    "audience": 70,
    "genre": "Romance",
    "movie_id": 1,
    "movie_name": "Zack and Miri Make a Porno",
    "profitability": 1.747541667,
    "rotten_tomatoes_score": 64,
    "studio": "The Weinstein Company",
    "timestamp": "2020-03-09T19:02:14.770674",
    "worldwide_gross": "$41.94 ",
    "year": 2008
  },
  {
    "audience": 52,
    "genre": "Comedy",
    "movie_id": 2,
    "movie_name": "Youth in Revolt",
    "profitability": 1.09,
    "rotten_tomatoes_score": 68,
    "studio": "The Weinstein Company",
    "timestamp": "2020-03-09T19:02:14.770674",
    "worldwide_gross": "$19.62 ",
    "year": 2010
  },
  {
    "audience": 35,
    "genre": "Comedy",
    "movie_id": 3,
    "movie_name": "You Will Meet a Tall Dark Stranger",
    ...
```

Get one movie by id:
```
$ curl -s -X GET --header 'Accept: application/json' 'http://localhost:5000/api/movie/4'
{
  "audience": 44,
  "genre": "Comedy",
  "movie_id": 4,
  "movie_name": "When in Rome",
  "profitability": 0.0,
  "rotten_tomatoes_score": 15,
  "studio": "Disney",
  "timestamp": "2020-03-09T19:02:14.770674",
  "worldwide_gross": "$43.04 ",
  "year": 2010
}
```

One movie partial representation:
```
$ curl -s -X GET --header 'Accept: application/json' 'http://localhost:5000/api/movie/6?fields=movie_name,year'
{
  "movie_name": "Water For Elephants",
  "year": 2011
}
```
