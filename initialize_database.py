import os
from config import db
from models import Movie

#TODO Make this read the csv file
# Data to initialize DB
MOVIES = [
    ["Zack and Miri Make a Porno", "Romance" ,"The Weinstein Company",70,1.747541667],
    ["Youth in Revolt","Comedy","The Weinstein Company",52,1.09],
    ["You Will Meet a Tall Dark Stranger","Comedy","Independent",35,1.211818182],
]

# Exit if the database exists
if os.path.exists("movies.db"):
    print("Database movies.db already exists")
    exit(0)

db.create_all()

# populate DB
for movie in MOVIES:
    m = Movie(movie_name=movie[0],
              genre=movie[1],
              studio=movie[2],
              audience=int(movie[3]),
              profitability=float(movie[4]))
    db.session.add(m)

db.session.commit()
