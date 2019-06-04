from beers.app.blueprints.api.models.beer_model import Beer
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients
from beers.tests.scripts.data import beers_data, ingredients_data


def populate_beers(amount):
    for r in range(0, amount):
        beer = Beer(
            beer_name=beers_data[r]['beer_name'],
            description=beers_data[r]['description'],
            color=beers_data[r]['color'],
            alcohol=beers_data[r]['alcohol'],
            temperature=beers_data[r]['temperature'],
            harmonization=beers_data[r]['harmonization']
        )
        beer.save()

        beer_id = beer.id
        for ingredient in ingredients_data[r]['ingredients'][0]['names']:
            ingredients = BeerIngredients(
                ingredient_name=ingredient,
                beer_id=beer_id
            )
            ingredients.save()
