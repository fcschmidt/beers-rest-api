import pytest
from beers.tests.utils.populate_data_base import populate_beers

from beers.tests.dictionaries.expected_beers_responses import (
    EXPECTED_DB_EMPTY,
    EXPECTED_BEER_NOT_EXIST,
    EXPECTED_KAISER_NOT_EXIST,
    EXPECTED_COLOR_NOT_EXIST,
    EXPECTED_ALCOHOL_NOT_EXIST,
    EXPECTED_TEMPERATURE_NOT_EXIST,
    EXPECTED_INGREDIENT_NOT_EXIST
    )

API_URL = '/api/v1/beers'


@pytest.mark.usefixtures('session')
class TestBeersAPIListFilterResponseSuccessfully:
    """Test Beers API Response List and Filter Items"""

    def test_get_not_beers(self, client):
        response = client.get(f'{API_URL}')
        assert response.status_code == 200
        response_json = response.get_json()
        assert response_json == EXPECTED_DB_EMPTY

    def test_get_beers(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}')
        assert response.status_code == 200
        response_json = response.get_json()
        assert len(response_json) == 3

    def test_filter_beer_by_name(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?beer_name=Skoll')
        assert response.status_code == 200

    def test_filter_beer_by_color(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?color=clara')
        assert response.status_code == 200
        resp_json = response.get_json()
        assert len(resp_json) == 2

    def test_filter_beer_by_alcohol(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?alcohol=3')
        assert response.status_code == 200

    def test_filter_beer_by_temperature(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?temperature=4')
        assert response.status_code == 200

    def test_filter_beer_by_ingredient(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?ingredient=cevada')
        assert response.status_code == 200
        response_json = response.get_json()
        assert len(response_json) == 3

    def test_get_beer(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}/1')
        assert response.status_code == 200
        response_json = response.get_json()
        assert response_json['id'] == 1


@pytest.mark.usefixtures('session')
class TestBeersAPIListFilterResponseErrors:
    """Test Beers API Response Errors List and Filter Items"""

    def test_get_beer_not_exist(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}/4')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_NOT_EXIST

    def test_filter_beer_by_name_not_exist(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?beer_name=kaiser')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_KAISER_NOT_EXIST

    def test_filter_beer_by_color_not_exist(self, client):
        populate_beers(3)
        response = client.get('/api/v1/beers?color=blue')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_COLOR_NOT_EXIST

    def test_filter_beer_by_alcohol_not_exist(self, client):
        populate_beers(3)
        response = client.get('/api/v1/beers?alcohol=10')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_ALCOHOL_NOT_EXIST

    def test_filter_beer_by_temperature_not_exist(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?temperature=55')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_TEMPERATURE_NOT_EXIST

    def test_filter_beer_by_ingredient_not_exist(self, client):
        populate_beers(3)
        response = client.get(f'{API_URL}?ingredient=uva')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_NOT_EXIST
