from datetime import datetime
from config import db, ma


class Movie(db.Model):
    __tablename__ = "movies"
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(128))
    genre = db.Column(db.String(32))
    studio = db.Column(db.String(64))
    audience = db.Column(db.Integer)
    profitability = db.Column(db.Float)
    rotten_tomatoes_score = db.Column(db.Integer)
    worldwide_gross = db.Column(db.String(16))
    year = db.Column(db.Integer)

    #Just for Internal information when updated
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie
        sqla_session = db.session
