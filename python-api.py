#################
# Python Get API
# As per request
# for the client
#########################
# Author: Fletcher Bayley
# Note: Created for Dan
# Sorry for being late!
# Desc: Quick Python API
# Date: 17/03/2021
#########################

from flask import Flask
from flask_restful import Resource, Api, reqparse

apl = Flask(__name__)
api = Api(apl)

class Numbers(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('num', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary

	if args['num'] % 7 == 0:
            return {
                'message': f"E"
            }, 200
	elif: 

	#return {'message': Welcome, enter your number."}, 200  # return msg & 200 OK


api.add_resource(Numbers, '/numbers')  # add endpoints

if __name__ == '__main__':
    apl.run()  # run the Flask application

