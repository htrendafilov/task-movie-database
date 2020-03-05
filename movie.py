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


def read_one(movie_id):
    """
    This function responds to a request for /api/movie/{movie_id}
    with one matching movie

    :param movie_id:   Id of the movie to find
    :return:            The found movie record
    """
    # Get the movie by id
    movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_none()

    # Did we find a movie?
    if movie is not None:

        # Serialize to JSON for the response
        movie_schema = MovieSchema()
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
