PARAMEDICS_INDEX_SETTINGS = {
    'settings': {},
    'mappings': {
        'paramedic': {
            'properties': {
                'name': { 'type': 'text' },
                'location': { 'type': 'geo_point' },
                'rating': { 'type': 'integer' },
                'specialization': { 'type': 'text' },
                'event_id': { 'type': 'text' },
                'type': { 'type': 'text' }
            }
        }
    }
}


EVENTS_INDEX_SETTINGS = {
    'settings': {},
    'mappings': {
        'event': {
            'properties': {
                'location': { 'type': 'geo_point' },
                'timestamp': { 'type': 'date' },
                'status': { 'type': 'text' },
                'event_type': { 'type': 'text' },
                'description': { 'type': 'text' }
            }
        }
    }
}
