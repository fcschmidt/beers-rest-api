from flask import Blueprint
from flask_restful import Api, reqparse, fields, Resource

from beers.app.blueprints.api.models.ingredients_model import BeerIngredients as IngredientsModel

from beers.app.blueprints.api.errors import error_does_not_exist, error_already_exists
from beers.app.blueprints.api.responses import resp_successfully

from beers.app.blueprints.api.utils import ingredients_serializer

bp = Blueprint('ingredients_api', __name__, url_prefix='/api/v1')
api = Api(bp)

ingredients_parser = reqparse.RequestParser()
ingredients_parser.add_argument('ingredient_name', type=str)
ingredients_parser.add_argument('beer_id', type=int)

resource_fields = {
    'id': fields.Integer,
    'ingredient_name': fields.String,
    'beer_id': fields.Integer,
}


class Ingredients(Resource):

    def __init__(self):
        self.ingredients_args = ingredients_parser.parse_args()

    def post(self):
        ingredient_name = self.ingredients_args['ingredient_name']
        beer_id = self.ingredients_args['beer_id']

        query_filter = IngredientsModel.filter_beer_id(beer_id)
        if not query_filter:
            error_does_not_exist(None, beer_id)

        serialized = ingredients_serializer(query_filter, True)
        for item in serialized:
            if item['ingredient_name'] == ingredient_name:
                return error_already_exists()

        ingredients = IngredientsModel(
            ingredient_name=ingredient_name,
            beer_id=beer_id
        )
        ingredients.save()
        return resp_successfully('Ingredient', 201)


class IngredientsItem(Resource):

    def __init__(self):
        self.ingredients_args = ingredients_parser.parse_args()

    def put(self, ingredient_id):
        ingredient_name = self.ingredients_args['ingredient_name']
        beer_id = self.ingredients_args['beer_id']

        query_ingredient = IngredientsModel.get_ingredient_id(ingredient_id)
        if not query_ingredient:
            return error_does_not_exist(None, ingredient_id)

        query_filter = IngredientsModel.filter_beer_id(beer_id)
        serialized = ingredients_serializer(query_filter, True)
        for item in serialized:
            if item['ingredient_name'] == ingredient_name:
                return error_already_exists()

        data = {
            'ingredient_name': ingredient_name,
            'beer_id': beer_id
        }
        IngredientsModel.update(query_ingredient, data)
        return resp_successfully('Ingredient', 201)

    @staticmethod
    def delete(ingredient_id):
        query_ingredient = IngredientsModel.get_ingredient_id(ingredient_id)
        if not query_ingredient:
            return error_does_not_exist(None, ingredient_id)

        query_ingredient.delete()
        return resp_successfully('Ingredient', 202)


def init_app(app):
    api.add_resource(Ingredients, '/ingredients', endpoint='ingredients')
    api.add_resource(IngredientsItem, '/ingredients/<int:ingredient_id>', endpoint='ingredient')
    app.register_blueprint(bp)
