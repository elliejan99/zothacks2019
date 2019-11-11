from flask_restful import Resource, reqparse
from db import mongo 
    
class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='name field cannot be left blank')
    parser.add_argument('year', type=str, required=True, help='year field cannot be left blank')
    parser.add_argument('housing', type=str, required=True, help='housing field cannot be left blank')
    parser.add_argument('interest', type=str, required=True, help='interest field cannot be left blank')
    parser.add_argument('value', type=str, required=True, help='value field cannot be left blank')

    def post(self):
        data = User.parser.parse_args()
        users = mongo.db.insert_one("name": data['name'], "year": data[year], "housing": data[housing],
            "interest": data[interest], "value": data[value])

