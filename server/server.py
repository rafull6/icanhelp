#!/usr/bin/env python3
from elasticsearch import Elasticsearch

from flask import Flask, request
from flask_restful import Resource, Api
from database_api.database_api import *


es_client = Elasticsearch(host='10.250.195.40', port=9200)
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
    def get(self, index_name):
        return get_objects_list(es_client,index_name)


class GetParamedicById(Resource):
    def get(self, paramedic_id):
        return get_object(es_client,"paramedics", paramedic_id)


class GetEventById(Resource):
    def get(self, event_id):
        return get_object(es_client, "events", event_id)


class ParamedicByDistance(Resource):
    def get(self, distance):
        json_data = request.get_json(force=True)
        location = json_data.get('location', {})
        lat = location.get('lat', None)
        lon = location.get('lon', None)
        if lat is None or lon is None:
            return {}
        return get_paramedics_in_distance(es_client, lat, lon, distance)


class UpdateObject(Resource):
    def post(self, object_type, object_id):
        json_data = request.get_json(force=True)


class AddObject(Resource):
    def post(self, object_type):
        json_data = request.get_json(force=True)


api.add_resource(ObjectsList, '/list/<index_name>')
api.add_resource(GetParamedicById, '/paramedic/<paramedic_id>')
api.add_resource(GetEventById, '/event/<event_id>')
api.add_resource(ParamedicByDistance, '/by_distance/<distance>')
api.add_resource(UpdateObject, '/update/<object_type>/<object_id>')
api.add_resource(AddObject, '/add/<object_type>')


if __name__ == '__main__':
    app.run(port='5000')
