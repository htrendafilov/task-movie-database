import os
import connexion
import pytest
from config import db
from models import Movie
import json

basedir = os.path.abspath(os.path.dirname(__file__))
app = connexion.FlaskApp(__name__, specification_dir=basedir)
app.add_api('swagger.yml')


@pytest.fixture(scope='module')
def client():
    # fetch underlying flask app from the connexion app
    flask_app = app.app
    flask_app.config["SQLALCHEMY_ECHO"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(flask_app)

    # create DB tables
    with flask_app.app_context():
        db.create_all()

    flask_app.config['DEBUG'] = True
    flask_app.config['TESTING'] = True

    with flask_app.test_client() as c:
        yield c


def test_read_all_empty(client):
    response = client.get('/api/movie')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert '[]' == response.data.decode('utf-8').strip()


def test_read_all_with_data(client):
    m = Movie(movie_name="Testing Movie",
              genre="NewGenre",
              studio="Test Studio",
              audience=90,
              profitability=0.34578,
              rotten_tomatoes_score=67,
              worldwide_gross="$23.34",
              year=2011
              )
    db.session.add(m)
    db.session.commit()

    response = client.get('/api/movie')
    movies_array = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert 1 == len(movies_array)
    assert "Testing Movie" == movies_array[0]['movie_name']
    assert 2011 == movies_array[0]['year']
