from beers.tests.scripts.populate_data_base import populate_beers

api_url = '/api/v1/ingredients'


def test_create_new_ingredient_not_exist_beer_id(client, session):
    populate_beers(3)
    new_ingredient = {
        'ingredient_name': 'aveia',
        'beer_id': 10
    }
    response = client.post(api_url, json=new_ingredient)
    assert response.status_code == 404

    expected = {
        'error': '10 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_create_new_ingredient_already_exists(client, session):
    populate_beers(3)
    new_ingredient = {
        'ingredient_name': 'cevada',
        'beer_id': 1
    }
    response = client.post(api_url, json=new_ingredient)
    assert response.status_code == 400

    expected = {
        'error': 'An ingredient with this name already exists.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_create_new_ingredient(client, session):
    populate_beers(3)
    new_ingredient = {
        'ingredient_name': 'mirtilo',
        'beer_id': 1
    }
    response = client.post(api_url, json=new_ingredient)
    assert response.status_code == 201

    expected = {
        'message': 'Ingredient created successfully!'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_delete_ingredient_not_exist(client, session):
    populate_beers(3)
    _id = 30
    response = client.delete(f'{api_url}/{_id}')
    assert response.status_code == 404

    expected = {
        'error': '30 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_delete_ingredient(client, session):
    populate_beers(3)
    _id = 1
    response = client.delete(f'{api_url}/{_id}')
    assert response.status_code == 202

    expected = {
        'message': 'Ingredient deleted successfully!'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_update_ingredient_not_exist(client, session):
    populate_beers(3)
    data = {
        'beer_id': 1,
        'ingredient_name': 'trigo'
    }
    _id = 50
    response = client.put(f'{api_url}/{_id}', json=data)
    assert response.status_code == 404

    expected = {
        'error': '50 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_update_ingredient_already_exist(client, session):
    populate_beers(3)
    data = {
        'beer_id': 1,
        'ingredient_name': 'cevada'
    }
    _id = 1
    response = client.put(f'{api_url}/{_id}', json=data)
    assert response.status_code == 400

    expected = {
        'error': 'An ingredient with this name already exists.'
    }
    resp_json = response.get_json()
    assert resp_json == expected


def test_update_ingredient(client, session):
    populate_beers(3)
    data = {
        'beer_id': 1,
        'ingredient_name': 'abacate'
    }
    _id = 1
    response = client.put(f'{api_url}/{_id}', json=data)
    assert response.status_code == 201

    expected = {
        'message': 'Ingredient created successfully!'
    }
    resp_json = response.get_json()
    assert resp_json == expected

