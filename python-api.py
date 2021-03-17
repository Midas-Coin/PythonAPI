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


api.add_resource(Numbers, '/numbers')  # add endpoints

if __name__ == '__main__':
    apl.run()  # run the Flask application

