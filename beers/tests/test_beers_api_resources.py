import pytest
from beers.tests.utils.populate_data_base import populate_beers

from beers.tests.dictionaries.beers_data_test import (
    NEW_BEER_DATA,
    UPDATE_BEER_DATA,
    UPDATE_BEER_NOT_EXIST,
    UPDATE_BEER_NOT_EXIST_INGREDIENT,
    )

from beers.tests.dictionaries.expected_responses import (
    EXPECTED_BEER_CREATED_SUCCESSFULLY,
    EXPECTED_BEER_UPDATE_SUCCESSFULLY,
    EXPECTED_BEER_DELETED_SUCCESSFULLY,
    EXPECTED_BEER_NOT_EXIST,
    EXPECTED_BEER_NOT_EXIST_INGREDIENT,
    EXPECTED_BEER_DETETE_NOT_EXIST
    )

API_URL = '/api/v1/beers'


@pytest.mark.usefixtures('session')
class TestBeersAPIResponseSuccessfully:
    """Test Beers API Response Successfully."""

    def test_create_new_beer(self, client):
        response = client.post(API_URL, json=NEW_BEER_DATA)
        assert response.status_code == 201
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_CREATED_SUCCESSFULLY

    def test_update_beer(self, client):
        populate_beers(3)
        response = client.put(f'{API_URL}/1', json=UPDATE_BEER_DATA)
        assert response.status_code == 200
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_UPDATE_SUCCESSFULLY

    def test_delete_beer(self, client):
        populate_beers(3)
        response = client.delete(f'{API_URL}/1')
        assert response.status_code == 202
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_DELETED_SUCCESSFULLY


@pytest.mark.usefixtures('session')
class TestBeersAPIResponseErrors:
    """Test Beers API Response Errors."""

    def test_update_beer_not_exist(self, client):
        populate_beers(2)
        response = client.put(f'{API_URL}/4', json=UPDATE_BEER_NOT_EXIST)
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_NOT_EXIST

    def test_update_beer_not_exist_ingredients(self, client):
        populate_beers(2)
        response = client.put(f'{API_URL}/1', json=UPDATE_BEER_NOT_EXIST_INGREDIENT)
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_NOT_EXIST_INGREDIENT

    def test_delete_beer_not_exist(self, client):
        populate_beers(3)
        response = client.delete(f'{API_URL}/10')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_DETETE_NOT_EXIST
