#!/usr/bin/env python3
from elasticsearch import Elasticsearch

from flask import Flask, request
from flask_restful import Resource, Api
from database_api.database_api import *


es_client = Elasticsearch(host='10.250.195.40', port=9200)
app = Flask(__name__)
api = Api(app)


"""
GET /list/<index_name> - returns list of (paramedics/events)<index_name>
GET /paramedic/<paramedic_id> - returns paramedic (single element list) with given _id<paramedic_id>
GET /event/<event_id> - returns event with given _id<event_id>
GET /by_distance/<distance> - (+ json) returns paramedics with distance lower than <distance>km to location specified in JSON:
                                                    {"location": { "lat": x, "lon": y }}
POST /update/<object_type>/<object_id> (+ json) - updates (paramedic/event)<object_type> with _id<object_id> with given JSON:
                                                    {"param_to_update": updated_value}
POST /add/<object_type> (+ json) - adds (paramedic/event)<object_type> to index with parameters from JSON
"""


class ObjectsList(Resource):
    def get(self, index_name):
        return get_objects_list(es_client, index_name)


class GetParamedicById(Resource):
    def get(self, paramedic_id):
        return get_object(es_client, "paramedics", paramedic_id)


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
        if object_type == 'paramedic':
            index_name = 'paramedics'
        elif object_type == 'event':
            index_name = 'events'
        else:
            return { 'result': False }
        result = update_doc(es_client, index_name=index_name, doc_id=object_id, update_data=json_data)
        return { 'result': result }


# TODO: add object query
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
