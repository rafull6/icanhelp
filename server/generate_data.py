#!/usr/bin/env python3
from elasticsearch import Elasticsearch
import argparse
import logging
import random

from indices_settings import PARAMEDICS_INDEX_SETTINGS, EVENTS_INDEX_SETTINGS


PARAMEDICS_INDEX = 'paramedics'
PARAMEDIC_DOC_TYPE = 'paramedic'
EVENTS_INDEX = 'events'
EVENT_DOC_TYPE = 'event'


def purge_indices(es_client: Elasticsearch):
    logger.info('Deleting ALL indices')
    es_client.indices.delete(index='*')


def create_indices_with_settings(es_client: Elasticsearch, index_name: str, settings: dict):
    es_client.indices.create(index=index_name, body=settings)


def post_to_elastic(es_client: Elasticsearch, index_name: str, doc_type: str, data_json: dict):
    logging.info('POST {}:{}'.format(index_name, data_json))
    es_client.index(index=index_name, doc_type=doc_type, body=data_json)


# TODO: single paramedic generator
def generate_paramedic():
    paramedic = {}
    return paramedic


# TODO: single event generator
def generate_event():
    event = {}
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
