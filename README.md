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
 - initilize_database.py - One-off script to be run to initialize the DB for the first time.
