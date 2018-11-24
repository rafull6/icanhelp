#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


"""
GET /list/<object_type>
GET /paramedic/<paramedic_id>
GET /event/<event_id>
GET /by_distance/<distance>
POST /update/<object_type>/<object_id> (+ json)
POST /add/<object_type> (+ json)
"""


class ObjectsList(Resource):
    def get(self, object_type):
        pass


class GetParamedicById(Resource):
    def get(self, paramedic_id):
        pass


class GetEventById(Resource):
    def get(self, event_id):
        pass


class ParamedicByDistance(Resource):
    def get(self, distance):
        pass


class UpdateObject(Resource):
    def post(self, object_type, object_id):
        json_data = request.get_json(force=True)


class AddObject(Resource):
    def post(self, object_type):
        json_data = request.get_json(force=True)


api.add_resource(ObjectsList, '/list/<object_type>')
api.add_resource(GetParamedicById, '/paramedic/<paramedic_id>')
api.add_resource(GetEventById, '/event/<event_id>')
api.add_resource(ParamedicByDistance, '/by_distance/<distance>')
api.add_resource(UpdateObject, '/update/<object_type>/<object_id>')
api.add_resource(AddObject, '/add/<object_type>')


if __name__ == '__main__':
    app.run(port='5000')
