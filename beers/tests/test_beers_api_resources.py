from beers.tests.utils.populate_data_base import populate_beers

api_url = '/api/v1/beers'


def test_create_new_beer(client, session):
    new_beer = {
        'beer_name': 'Skoll',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'color': 'clara',
        'alcohol': '3',
        'temperature': '4',
        'ingredients': [
            {'names': ['cevada', 'lupulo', 'malte', 'trigo']}
        ]
    }
    response = client.post(api_url, json=new_beer)
    assert response.status_code == 201

    resp_json = response.get_json()
    expected = {
        'message': 'Beer created successfully!'
    }
    assert resp_json == expected


def test_update_beer_not_exist(client, session):
    populate_beers(2)
    update_beer = {
        'beer_name': 'Skoll',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'color': 'clara',
        'alcohol': '3',
        'temperature': '4',
        'ingredients': {
            'list': [
                {'ingredient_name': 'cevada', 'id': 1},
                {'ingredient_name': 'lupulo', 'id': 2},
                {'ingredient_name': 'malte', 'id': 3},
            ]
        }
    }
    _id = 4
    response = client.put(f'{api_url}/{_id}', json=update_beer)
    assert response.status_code == 404

    expected = {
        'error': '4 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_update_beer_not_exist_ingredients(client, session):
    populate_beers(2)
    update_beer = {
        'beer_name': 'Skoll',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'color': 'clara',
        'alcohol': '3',
        'temperature': '4',
        'ingredients': {
            'list': [
                {'ingredient_name': 'cevada', 'id': 55},
                {'ingredient_name': 'lupulo', 'id': 100},
                {'ingredient_name': 'malte', 'id': 49},
            ]
        }
    }
    _id = 1
    response = client.put(f'{api_url}/{_id}', json=update_beer)
    assert response.status_code == 404

    expected = {
        'error': '55 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_update_beer(client, session):
    populate_beers(3)
    update_beer = {
        'beer_name': 'Adriática',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
        'color': 'clara',
        'alcohol': '5',
        'temperature': '5',
        'ingredients': {
            'list': [
                {'ingredient_name': 'cevada', 'id': 1},
                {'ingredient_name': 'lupulo', 'id': 2},
                {'ingredient_name': 'malte', 'id': 3},
            ]
        }
    }
    _id = 1
    response = client.put(f'{api_url}/{_id}', json=update_beer)
    assert response.status_code == 200

    expected = {
        'message': 'Beer updated successfully!'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_delete_beer_not_exist(client, session):
    populate_beers(3)
    _id = 10
    response = client.delete(f'{api_url}/{_id}')
    assert response.status_code == 404

    expected = {
        'error': '10 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_delete_beer(client, session):
    populate_beers(3)
    _id = 1
    response = client.delete(f'{api_url}/{_id}')
    assert response.status_code == 202

    expected = {
        'message': 'Beer deleted successfully!'
    }
    resp_json = response.get_json()
    assert resp_json == expected
