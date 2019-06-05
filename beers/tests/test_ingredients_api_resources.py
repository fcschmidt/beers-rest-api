import pytest
from beers.tests.utils.populate_data_base import populate_beers

from beers.tests.dictionaries.ingredients_data_test import (
    NEW_INGREDIENT,
    UPDATE_INGREDIENT_DATA,
    NEW_INGREDIENT_NOT_EXIST_DATA,
    INGREDIENT_ALREADY_EXISTS,
    )

from beers.tests.dictionaries.ingredients_expected_responses import (
    EXPECTED_INGREDIENT_CREATED_SUCCESSFULLY,
    EXPECTED_INGREDIENT_UPDATED_SUCCESSFULLY,
    EXPECTED_INGREDIENT_DELETED_SUCCESSFULLY,
    EXPECTED_INGREDIENT_NOT_EXIST,
    EXPECTED_BEER_NOT_EXIST,
    EXPECTED_INGREDIENT_ALREADY_EXISTS,
    EXPECTED_INGREDIENT_UPDATED_NOT_EXIST
    )

API_URL = '/api/v1/ingredients'


@pytest.mark.usefixtures('session')
class TestIngredientsAPIResponseSuccessfully:
    """Test Ingredients API Response Successfully."""

    def test_create_new_ingredient(self, client):
        populate_beers(3)
        response = client.post(API_URL, json=NEW_INGREDIENT)
        assert response.status_code == 201
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_CREATED_SUCCESSFULLY

    def test_update_ingredient(self, client):
        populate_beers(3)
        response = client.put(f'{API_URL}/1', json=UPDATE_INGREDIENT_DATA)
        assert response.status_code == 201
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_UPDATED_SUCCESSFULLY

    def test_delete_ingredient(self, client):
        populate_beers(3)
        response = client.delete(f'{API_URL}/1')
        assert response.status_code == 202
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_DELETED_SUCCESSFULLY


@pytest.mark.usefixtures('session')
class TestIngredientsAPIResponseErrors:
    """Test Ingredients API Response Errors."""

    def test_create_new_ingredient_not_exist_beer_id(self, client):
        populate_beers(3)
        response = client.post(API_URL, json=NEW_INGREDIENT_NOT_EXIST_DATA)
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_BEER_NOT_EXIST

    def test_create_new_ingredient_already_exists(self, client):
        populate_beers(3)
        response = client.post(API_URL, json=INGREDIENT_ALREADY_EXISTS)
        assert response.status_code == 400
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_ALREADY_EXISTS

    def test_update_ingredient_not_exist(self, client):
        populate_beers(3)
        response = client.put(f'{API_URL}/30', json=EXPECTED_INGREDIENT_UPDATED_NOT_EXIST)
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_NOT_EXIST

    def test_update_ingredient_already_exist(self, client):
        populate_beers(3)
        response = client.put(f'{API_URL}/1', json=INGREDIENT_ALREADY_EXISTS)
        assert response.status_code == 400
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_ALREADY_EXISTS

    def test_delete_ingredient_not_exist(self, client):
        populate_beers(3)
        response = client.delete(f'{API_URL}/30')
        assert response.status_code == 404
        response_json = response.get_json()
        assert response_json == EXPECTED_INGREDIENT_NOT_EXIST
