from beers.app.blueprints.api.models.beer_model import Beer
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients

from beers.tests.dictionaries.beers_populate_data_test import BEERS_DATA
from beers.tests.dictionaries.ingredients_populate_data_test import INGREDIENTS_DATA


def populate_beers(amount):
    for r in range(0, amount):
        beer = Beer(
            beer_name=BEERS_DATA[r]['beer_name'],
            description=BEERS_DATA[r]['description'],
            color=BEERS_DATA[r]['color'],
            alcohol=BEERS_DATA[r]['alcohol'],
            temperature=BEERS_DATA[r]['temperature'],
            harmonization=BEERS_DATA[r]['harmonization']
        )
        beer.save()

        beer_id = beer.id
        for ingredient in INGREDIENTS_DATA[r]['ingredients'][0]['names']:
            ingredients = BeerIngredients(
                ingredient_name=ingredient,
                beer_id=beer_id
            )
            ingredients.save()
