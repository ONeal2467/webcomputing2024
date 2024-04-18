from config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255))
    description = db.Column(db.String(255))
    menu_items = db.relationship('MenuItem', backref='restaurant', lazy='dynamic')

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)  # Reference to MenuItem

    # Optional: relationships to clearly define reverse access from User and MenuItem
    user = db.relationship('User', backref=db.backref('favorites', lazy=True))
    menu_item = db.relationship('MenuItem', backref=db.backref('favorited_by', lazy=True))
