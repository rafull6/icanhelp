#!/usr/bin/env python3

def get_objects_list(es_client, index_name):
    query = {
        "query": {"match_all": {}},
        "size": 100
    }
    result = es_client.search(index=index_name, body=query).get(
        "hits", {}
    ).get(
        "hits", {}
    )
    return result

def get_object(es_client, index_name, object_index):
    query = {
        "query": {
            "terms": {
                "_id" : object_index
            }
        }
    }
    result = es_client.search(index=index_name, body=query).get(
        "hits", {}
    ).get(
        "hits", {}
    )
    return result
