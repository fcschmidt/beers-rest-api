from beers.tests.scripts.populate_data_base import populate_beers


def test_get_not_beers(client, session):
    response = client.get('/api/v1/beers')
    assert response.status_code == 200

    expected = {
        'message': 'Data base empty!'
    }
    resp_json = response.get_json()
    assert resp_json['message'] == expected['message']


def test_get_beers(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers')
    assert response.status_code == 200


def test_filter_beer_by_name_not_exist(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?beer_name=kaiser')
    assert response.status_code == 404

    expected = {
        'error': 'kaiser does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json['error'] == expected['error']


def test_filter_beer_by_name(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?beer_name=Skoll')
    assert response.status_code == 200


def test_filter_beer_by_color_not_exist(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?color=azul')
    assert response.status_code == 404


def test_filter_beer_by_color(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?color=clara')
    assert response.status_code == 200


def test_filter_beer_by_alcohol_not_exist(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?alcohol=10')
    assert response.status_code == 404


def test_filter_beer_by_alcohol(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?alcohol=3')
    assert response.status_code == 200


def test_filter_beer_by_temperature_not_exist(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?temperature=10')
    assert response.status_code == 404


def test_filter_beer_by_temperature(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?temperature=4')
    assert response.status_code == 200


def test_filter_beer_by_ingredient_not_exist(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?ingredient=uva')
    assert response.status_code == 404


def test_filter_beer_by_ingredient(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers?ingredient=cevada')
    assert response.status_code == 200

    resp_json = response.get_json()
    assert len(resp_json) == 3


def test_get_beer_not_exist(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers/10')
    assert response.status_code == 404

    expected = {
        'error': '10 does not exist.'
    }
    resp_json = response.get_json()
    assert resp_json['error'] == expected['error']


def test_get_beer(client, session):
    populate_beers(3)
    response = client.get('/api/v1/beers/1')
    assert response.status_code == 200

    resp_json = response.get_json()
    assert resp_json['id'] == 1
