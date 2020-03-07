import os
import connexion
import pytest

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

    from config import db
    db.init_app(flask_app)

    # create DB tables
    with flask_app.app_context():
        db.create_all()

    flask_app.config['DEBUG'] = True
    flask_app.config['TESTING'] = True

    with flask_app.test_client() as c:
        yield c


def test_read_all(client):
    response = client.get('/api/movie')
    assert response.status_code == 200