#!/usr/bin/env python3

from flask import Flask, make_response,jsonify
from flask_migrate import Migrate

from models import db, Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>HOME PAGE</h1>'

@app.route('/restaurants')
def restaurants():
    restaurant = Restaurant.query.all()
    data_format = [rest.to_dict() for rest in restaurant]

    response = make_response(
        jsonify(data_format),
        200
    )
    return response



if __name__ == '__main__':
    app.run(port=5555)
