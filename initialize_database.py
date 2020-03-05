import os
import csv
from config import db
from models import Movie

# Exit if the database exists
if os.path.exists("movies.db"):
    print("Database movies.db already exists")
    exit(0)

db.create_all()

# populate DB
with open('initialization_data/movies.csv') as csvfile:
    movies_table = csv.reader(csvfile)
    processing_first_row = True
    for movie in movies_table:
        if processing_first_row:
            processing_first_row = False
            continue
        m = Movie(movie_name=movie[0],
                  genre=movie[1],
                  studio=movie[2],
                  audience=int(movie[3]),
                  profitability=float(movie[4]),
                  rotten_tomatoes_score=int(movie[5]),
                  worldwide_gross = movie[6],
                  year = int(movie[7])
        )
        db.session.add(m)

db.session.commit()
