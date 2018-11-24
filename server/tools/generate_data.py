#!/usr/bin/env python3
from elasticsearch import Elasticsearch
import argparse
import logging
import random
import datetime

from indices_settings import PARAMEDICS_INDEX_SETTINGS, EVENTS_INDEX_SETTINGS


PARAMEDICS_INDEX = 'paramedics'
PARAMEDIC_DOC_TYPE = 'paramedic'
EVENTS_INDEX = 'events'
EVENT_DOC_TYPE = 'event'
NAMES = ["Julia","Zuzanna", "Maja","Alicja", "Maria", "Jakub", "Jan", "Szymon", "Bartosz", "Dawid"]
SURNAMES = ["Nowak", "Wojcik", "Kowalczyk", "Wozniak", "Mazur", "Krawczyk", "Wieczorek", "Adamczyk", "Dudek", "Pawlak"]
PARAMEDIC_TYPES = ["ambulance", "human"]
LAT_MIN = 52192740
LON_MIN = 20930010
LAT_MAX = 52295380
LON_MAX = 21126760


def purge_indices(es_client: Elasticsearch):
    logger.info('Deleting ALL indices')
    es_client.indices.delete(index='*')


def create_indices_with_settings(es_client: Elasticsearch, index_name: str, settings: dict):
    es_client.indices.create(index=index_name, body=settings)


def post_to_elastic(es_client: Elasticsearch, index_name: str, doc_type: str, data_json: dict):
    logging.info('POST {}:{}'.format(index_name, data_json))
    es_client.index(index=index_name, doc_type=doc_type, body=data_json)


def generate_name():
    return random.choice(NAMES) + " " + random.choice (SURNAMES)


def generate_location():
    return {
        "lat" : random.randrange(LAT_MIN, LAT_MAX) / 1000000,
        "lon" : random.randrange(LON_MIN, LON_MAX) / 1000000
    }


def generate_paramedic():
    paramedic = {
        "name" : generate_name(),
        "location" : generate_location(),
        "rating" : random.randrange(1,5),
        "specialization" : random.choice(["sercownik", "kostnik", "strazak", "policjant"]) ,
        "event_id" : "",
        "type" :  PARAMEDIC_TYPES[0] if random.random() > 0.9 else PARAMEDIC_TYPES[1]
        "phone" : str(random.randint(1e9,9e9))

    }
    return paramedic


def generate_event():
    timestamp = datetime.datetime.now() + datetime.timedelta(seconds=random.randint(-3600,3600));
    event = {
        "location" : generate_location(),
        "status" : "default",
        "event_type" : random.choice(["heart attack","accident","epilepsy","choking","haemorrhage","fracture"]),
        "description" : "",
        "timestamp" : timestamp
    }
    return event



logger = logging.getLogger('data_generator')
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)


args_parser = argparse.ArgumentParser(description='Data generator for "I can help you"')
args_parser.add_argument('--host', default='10.250.195.40')
args_parser.add_argument('--port', type=int, default=9200)
args = args_parser.parse_args()
HOST = args.host
PORT = args.port
logger.info('Using endpoint: {}:{}'.format(
    HOST, PORT
))

es_client = Elasticsearch(host='10.250.195.40', port=9200)
logger.info('Elasticsearch client for endpoint {}:{} created'.format(
    HOST, PORT
))
if not es_client.ping():
    raise EnvironmentError('Database is unreachable!')
logger.info('Elasticsearch is UP and ready!')

purge_indices(es_client)
create_indices_with_settings(es_client, PARAMEDICS_INDEX, PARAMEDICS_INDEX_SETTINGS)
create_indices_with_settings(es_client, EVENTS_INDEX, EVENTS_INDEX_SETTINGS)

for _ in range(0, 32):
    post_to_elastic(
        es_client=es_client,
        index_name=PARAMEDICS_INDEX,
        doc_type=PARAMEDIC_DOC_TYPE,
        data_json=generate_paramedic()
    )

for _ in range(0, 5):
    post_to_elastic(
        es_client=es_client,
        index_name=EVENTS_INDEX,
        doc_type=EVENT_DOC_TYPE,
        data_json=generate_event()
    )
