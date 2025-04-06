from flask_sqlalchemy import SQLAlchemy

from utils.db import db

db = SQLAlchemy()
# parent table
class Countrytable(db.Model):
    Rank = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.String(255), nullable=False)
    Cost_Of_Living = db.Column(db.Integer, nullable=False)
    Rent_Index = db.Column(db.Integer, nullable=False)
    Groceries_Index = db.Column(db.Integer, nullable=False)
    Restaurant_Index = db.Column(db.Integer, nullable=False)
    Local_Purchase = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Country {self.Country}>"