from ..scripts.populate_data_base import populate_beers

api_url = {
    'beers': '/api/v1/beers',
    'ingredients': '/api/v1/ingredients'
}


def test_create_new_ingredient_and_check_response(client, session):
    populate_beers(3)
    beer_response = client.get(f"{api_url['beers']}/1")
    assert beer_response.status_code == 200

    beer_resp_json = beer_response.get_json()
    beer_id = beer_resp_json['id']

    new_data = {
        'ingredient_name': 'banana',
        'beer_id': beer_id
    }
    expected = {
        'message': 'Ingredient created successfully!'
    }

    response = client.post(f"{api_url['ingredients']}", json=new_data)
    resp_json = response.get_json()
    assert response.status_code == 201
    assert resp_json == expected


def test_delete_ingredient_and_check_response(client, session):
    pass
