# Technical Challenge: DE Junior
This project is designed to resolve the Technical Challenge for a DE Junior position.

### Technologies Used
* Python
* Supabase
* Typesense

### Libraries
* SQLAlchemy
* FastAPI
* Poetry
* Pydantic
* Uvicorn
  
### Setup
This repository includes a docker-compose file to run Typesense locally. Additionally, you need to unzip the typesense-data archive to use the Tracks collection.

### Example Request
Here is an example of the body for making a request to find a track using Typesense:
```json
{
    "query": "war",
    "query_items": "title",
    "filter_items": [
        {
            "field": "artist",
            "value": [
                "Pink Floyd"
            ]
        },
        {
            "field": "release_decade",
            "value": [
                "1980s"
            ]
        }
    ],
    "sort_direction": "asc"
}
```
When making a request, the query and query_items fields are required, while the other fields are optional. In the query field, you must enter the word or phrase that you want to search for. In the query_items field, you specify the fields where TypeSense will search for the phrase you provided in the query field. You can choose from title, artist, album, or a combination of these.

In the sort_direction field, you can only choose between asc or desc because the results can only be sorted by release_year. Finally, the filter_items field is a list of objects where you specify the field you want to use to filter the results, and in the value field, you list the values you want to search for. If you choose a numeric field, you need to add the operator, for example, < or >.
