from flask import Flask, render_template
from flask_restful import Api
from flask_pymongo import PyMongo
from pymongo import MongoClient 
from flask_restful import Resource, reqparse
from db import mongo 

#from users.py import User

app = Flask(__name__)

text = "/Users/eijan/Documents/zothacks2019/result1.txt"

with open(text) as results:
    line = results.read()

@app.route('/zothacks2019/')
def user():
    return render_template('results.html', line)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
api = Api(app)

api.add_resource(User, '/zothacks2019/')

if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port = 5000, debug = True)
    