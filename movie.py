"""
This is the module for our REST actions
"""

from flask import abort
from config import db
from models import Movie, MovieSchema


def read_all():
    """
    This function responds to a request for /api/movie
    with the complete lists of movies

    :return:        json string of list of movies
    """
    # Get the list of movies from our DB
    movies = Movie.query.order_by(Movie.movie_id).all()

    # Serialize for the response
    movie_schema = MovieSchema(many=True)
    return movie_schema.dump(movies)

def read_one(**kwargs):
    """
    This function responds to a request for /api/movie/{movie_id}
    with one matching movie.
    Optionally comma separated fields could be supplied for partial representation:
    Example: /api/movie/{movie_id}?fields=movie_name,year

    :param kwargs:   Arguments map, where 'movie_id' is required and 'fields' is optional
    :return:            The found movie record
    """
    # Get the movie by id
    movie_id = kwargs['movie_id']
    fields = kwargs.get('fields')
    movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_none()

    # Did we find a movie?
    if movie is not None:
        #TODO: Validate fields values if correct
        movie_schema = MovieSchema(only=fields.split(',')) if fields else MovieSchema()
        # Serialize to JSON for the response
        return movie_schema.dump(movie)

    # Otherwise, nope, didn't find that movie
    else:
        abort(
            404,
            "Movie not found for Id: {movie_id}".format(movie_id=movie_id),
        )


def create(movie):
    """
    This function creates a new movie record in the DB

    :param movie:  New movie record to create
    :return:        201 on success
    """
    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)

    # Add the new movie record to the database
    db.session.add(new_movie)
    db.session.commit()

    # Return the newly created record in the response
    data = schema.dump(new_movie)

    return data, 201

def update(movie_id, movie):
    """
    This function updates an existing movie in the database

    :param movie_id:   Id of the movie to be updated
    :param movie:      The new Movie object
    :return:            updated movie structure
    """
    # Get the movie requested from the db into session
    update_movie = Movie.query.filter(
        Movie.movie_id == movie_id
    ).one_or_none()

    # Are we trying to find a movie that does not exist?
    if update_movie is None:
        abort(
            404,
            "Movie not found for Id: {movie_id}".format(movie_id=movie_id),
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in movie into a db object
        schema = MovieSchema()
        update = schema.load(movie, session=db.session)

        # Set the id to the movie we want to update
        update.movie_id = update_movie.movie_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated movie in the response
        data = schema.dump(update_movie)

        return data, 200


def delete(movie_id):
    """
    This function deletes a movie from the Database
	The method will always succeed, because we want idempotent delete

    :param movie_id:   Id of the movie to delete
    :return:            200
    """
    # Get the movie requested
    movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_none()

    if movie is not None:
        db.session.delete(movie)
        db.session.commit()

    return "", 200
