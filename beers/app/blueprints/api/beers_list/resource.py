from flask import Blueprint
from flask_restful import Api, reqparse, fields, Resource

from beers.app.blueprints.api.models.beer_model import Beer as BeerModel
from beers.app.blueprints.api.models.ingredients_model import BeerIngredients as IngredientsModel

from beers.app.blueprints.api.utils import (
    beers_serializer,
    serializer,
    add_ingredients,
    parser_beers,
    ingredients_serializer
    )

from beers.app.blueprints.api.responses import resp_empty_data_base, resp_content_successfully
from beers.app.blueprints.api.errors import error_does_not_exist

bp = Blueprint('rest_api', __name__, url_prefix='/api/v1')
api = Api(bp)


beers_parser = reqparse.RequestParser()
beers_parser.add_argument('beer_name', type=str)
beers_parser.add_argument('description', type=str)
beers_parser.add_argument('harmonization', type=str)
beers_parser.add_argument('color', type=str)
beers_parser.add_argument('alcohol', type=str)
beers_parser.add_argument('temperature', type=str)

resource_fields_beer = {
    'id': fields.Integer,
    'beer_name': fields.String,
    'description': fields.String,
    'harmonization': fields.String,
    'color': fields.String,
    'alcohol': fields.String,
    'temperature': fields.String
}


ingredients_parser = reqparse.RequestParser()
ingredients_parser.add_argument('ingredient', type=str)

resource_fields_ingredients = {
    'id': fields.Integer,
    'ingredient_name': fields.String,
    'beer_id': fields.Integer,
}


class ListFilterBeers(Resource):

    def __init__(self):
        self.beer_args = beers_parser.parse_args()
        self.ingredients_args = ingredients_parser.parse_args()

    def get(self):
        beer_name = self.beer_args['beer_name']
        color = self.beer_args['color']
        alcohol = self.beer_args['alcohol']
        temperature = self.beer_args['temperature']
        ingredient = self.ingredients_args['ingredient']

        query_beers = BeerModel.get_beers()
        serialized = beers_serializer(query_beers, True)
        if not query_beers:
            return resp_empty_data_base()

        if beer_name:
            query_name = BeerModel.filter_beer_name(beer_name)
            error_does_not_exist(query_name, beer_name)
            serialized = serializer(query_name)
            return resp_content_successfully(serialized)

        if color:
            query_color = BeerModel.filter_beer_color(color)
            error_does_not_exist(query_color, color)
            serialized = serializer(query_color)
            return resp_content_successfully(serialized)

        if alcohol:
            query_alcohol = BeerModel.filter_beer_alcohol(alcohol)
            error_does_not_exist(query_alcohol, alcohol)
            serialized = serializer(query_alcohol)
            return resp_content_successfully(serialized)

        if temperature:
            query_temperature = BeerModel.filter_beer_temperature(temperature)
            error_does_not_exist(query_temperature, temperature)
            serialized = serializer(query_temperature)
            return resp_content_successfully(serialized)

        if ingredient:
            query_ingredient = IngredientsModel.filter_ingredient_name(ingredient)
            error_does_not_exist(query_ingredient, ingredient)
            serialized = add_ingredients(query_beers, serialized)
            response_parser = parser_beers(serialized, ingredient)
            return resp_content_successfully(response_parser)

        serialized = add_ingredients(query_beers, serialized)
        return resp_content_successfully(serialized)


class BeerItem(Resource):

    def __init__(self):
        self.beer_args = beers_parser.parse_args()
        self.ingredients_args = ingredients_parser.parse_args()

    @staticmethod
    def get(beer_id):
        query_beer = BeerModel.get_beer_id(beer_id)
        if not query_beer:
            error_does_not_exist(None, beer_id)

        serialized = beers_serializer(query_beer, False)
        query_filter = IngredientsModel.filter_beer_id(beer_id)

        count = 0
        ingredients_list = []
        for item in query_filter:
            ingredients_list.append(ingredients_serializer(item, False))
            serialized['ingredients'] = ingredients_list
            count += 1
        return resp_content_successfully(serialized)


def init_app(app):
    api.add_resource(ListFilterBeers, '/beers', endpoint='beers_list')
    api.add_resource(BeerItem, '/beers/<int:beer_id>', endpoint='beer_item')
    app.register_blueprint(bp)
