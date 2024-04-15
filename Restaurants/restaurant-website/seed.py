from app import db
from app.models import Restaurant, Menu, Item

def seed_database():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Add restaurants
    golden_corral = Restaurant(
        name="Golden Corral", 
        location="123 Buffet Dr, Eatville, USA", 
        rating=4.2, 
        busy_indicator="Moderately Busy"
    )
    mcdonalds = Restaurant(
        name="McDonald's", 
        location="456 Fast Food Ln, Speedy City, USA", 
        rating=3.8, 
        busy_indicator="Highly Busy"
    )

    # Add them to the session
    db.session.add
