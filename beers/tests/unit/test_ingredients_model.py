import pytest
from beers.tests.scripts.populate_data_base import populate_beers
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients
from beers.app.blueprints.api.models.beer_model import Beer
from beers.tests.scripts.data import beers_data, ingredients_data
from beers.app.blueprints.api.utils import ingredients_serializer


@pytest.mark.usefixtures('session')
class TestIngredientsModel:

    def test_create_ingredients(self):
        populate_beers(3)
        get_ingredients = BeerIngredients.get_ingredient_id(1)
        assert get_ingredients.id == 1
        assert get_ingredients.ingredient_name == 'cevada'

    def test_delete_ingredients(self):
        populate_beers(3)
        query_ingredients = BeerIngredients.filter_beer_id(1)
        for query in query_ingredients:
            ingredient = BeerIngredients.get_ingredient_id(query.id)
            ingredient.delete()
        query_ingredients = BeerIngredients.filter_beer_id(1)
        assert len(query_ingredients) == 0

    def test_update_ingredients(self):
        populate_beers(3)
        new_beers = beers_data[1]
        new_ingredients = ingredients_data[2]['ingredients'][0]['names']

        query_beer = Beer.get_beer_id(2)
        query_ingredients = BeerIngredients.filter_beer_id(query_beer.id)
        count = 0
        for ingredient in new_ingredients:
            data_ingredients = {
                'ingredient_name': ingredient,
                'beer_id': query_beer.id
            }
            query_ingredient = query_ingredients[count]
            BeerIngredients.update(query_ingredient, data_ingredients)
            count += 1

        Beer.update(query_beer, new_beers)

        query_update_ingredients = BeerIngredients.filter_beer_id(query_beer.id)
        serialized = ingredients_serializer(query_update_ingredients, True)
        for r in range(0, len(serialized)):
            assert serialized[r]['ingredient_name'] == new_ingredients[r]

    def test_get_ingredients(self):
        populate_beers(3)
        query_ingredients = BeerIngredients.get_ingredients()
        serialized = ingredients_serializer(query_ingredients, True)
        assert serialized[0]['beer_id'] == 1
        assert serialized[0]['ingredient_name'] == 'cevada'

    def test_get_ingredient_by_id(self):
        populate_beers(3)
        query_ingredient = BeerIngredients.get_ingredient_id(1)
        serialized = ingredients_serializer(query_ingredient, False)
        assert serialized['beer_id'] == 1
        assert serialized['ingredient_name'] == 'cevada'

    def test_filter_ingredients_by_name(self):
        populate_beers(3)
        query_ingredients = BeerIngredients.filter_ingredient_name('cevada')
        serialized = ingredients_serializer(query_ingredients, True)
        expected = [
            {'beer_id': 1, 'id': 1, 'ingredient_name': 'cevada'},
            {'beer_id': 2, 'id': 5, 'ingredient_name': 'cevada'},
            {'beer_id': 3, 'id': 8, 'ingredient_name': 'cevada'}
        ]
        assert len(serialized) == 3
        for i in range(0, 3):
            assert serialized[i] == expected[i]

    def test_filter_by_beer_id(self):
        populate_beers(3)
        query_beer_id = BeerIngredients.filter_beer_id(1)
        serialized = ingredients_serializer(query_beer_id, True)
        assert serialized[0]['beer_id'] == 1
