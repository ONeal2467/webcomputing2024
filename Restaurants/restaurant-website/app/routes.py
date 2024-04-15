from flask import render_template
from app import app, db
from app.models import Restaurant, Menu, Item

@app.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)

@app.route('/restaurant/<int:id>')
def restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    menu = Menu.query.filter_by(restaurant_id=id).first()
    return render_template('restaurant.html', restaurant=restaurant, menu=menu)
