def get_paramedics_in_distance(es_client, lat, lon, distane):
    query = {
        'query': {
            'bool': {
                'must': {
                    'match_all': {}
                },
                'filter': {
                    'geo_distance': {
                        'distance': '{}km'.format(distane),
                        'location': {
                            'lat': lat,
                            'lon': lon
                        }
                    }
                }
            }
        }
    }
    results = es_client.search(index='paramedics', body=query).get('hits', {}).get('hits', {})
    return results


def get_objects_list(es_client, index_name):
    query = {
        'query': {'match_all': {}},
        'size': 100
    }
    results = es_client.search(index=index_name, body=query).get('hits', {}).get('hits', {})
    return results


def get_object(es_client, index_name, object_index):
    query = {
        'query': {
            'terms': {
                '_id': [object_index]
            }
        }
    }
    results = es_client.search(index=index_name, body=query).get('hits', {}).get('hits', {})
    return results


def update_doc(es_client, index_name, doc_id, update_data):
    result = es_client.update(index=index_name, id=doc_id, body=update_data)
    return result.get('result', False)
