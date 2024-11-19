from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    image_url = db.Column(db.String)
    rating = db.Column(db.Float)
    year = db.Column(db.Integer)

