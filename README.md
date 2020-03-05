# uIMDB Movie Database task

## Description
The task is to implement very, very, veru simplified IMDB like movie database.
It should:
  - store the movie data in a database
  - Have REST API to query, create and update movie record
  - initialize the database if empty from ...
  - use watever technology stack
  
 Full description (in Bulgarian) is in documents/task_definition.txt
 
## Design Overview

I decided to do it Python, but will give it a shot also in Java later.

I decided on Flask as the WEB framework
Used Swagger to describe the rest API and used connexion for this purpose
SQLAlchemy is used for ORM and Marshmallow for object serialization/deserialization to JSON
