from beers.app.blueprints.api.schemas import BeerSchema, BeerIngredientsSchema
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients as IngredientsModel

beers_schema = BeerSchema()


def beers_serializer(content, state):
    serialized = beers_schema.dump(content, many=state).data
    return serialized


ingredients_schema = BeerIngredientsSchema()


def ingredients_serializer(content, state):
    serialized = ingredients_schema.dump(content, many=state).data
    return serialized


def serializer(query):
    serialized = beers_serializer(query, True)
    serialized = add_ingredients(query, serialized)
    return serialized


def add_ingredients(query, serialized):
    count = 0
    ingredients_list = []
    for beer in query:
        query_filter = IngredientsModel.filter_beer_id(beer.id)
        if query_filter:
            ingredients_list.append(ingredients_serializer(query_filter, True))
            serialized[count]['ingredients'] = ingredients_list[0]
            count += 1
            ingredients_list = []
    return serialized


def parser_beers(serialized, name):
    beers = []
    for beer in serialized:
        for ingredient in beer['ingredients']:
            if ingredient['ingredient_name'] == name:
                beers.append(beer)
    return beers


