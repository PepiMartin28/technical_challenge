from core.typesense_client import client

schema = {
    'name': 'tracks',
    'fields': [
        {'name': 'title', 'type': 'string', 'facet': False},  
        {'name': 'artist', 'type': 'string[]', 'facet': True},
        {'name': 'album', 'type': 'string', 'facet': False},
        {'name': 'release_type', 'type': 'string', 'facet': True},
        {'name': 'release_year', 'type': 'int32', 'facet': False},
        {'name': 'release_decade', 'type': 'string', 'facet': True}, 
        {'name': 'release_country', 'type': 'string', 'facet': True}  
    ],
    'default_sorting_field': 'release_year'
}


client.collections.create(schema)

