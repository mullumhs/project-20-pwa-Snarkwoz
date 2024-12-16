from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String)
    genre = db.Column(db.String)
    image_url = db.Column(db.String)
    rating = db.Column(db.Float)
    year = db.Column(db.Integer)
    description = db.Column(db.String)

