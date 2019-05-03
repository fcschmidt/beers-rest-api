from marshmallow import fields, Schema


class BeerSchema(Schema):
    id = fields.Integer(dump_only=True)
    beer_name = fields.String(dump_only=True)
    description = fields.String(dump_only=True)
    harmonization = fields.String(dump_only=True)
    color = fields.String(dump_only=True)
    alcohol = fields.String(dump_only=True)
    temperature = fields.String(dump_only=True)
    ingredients = fields.String(dump_only=True)

    class Meta:
        strict = True


class BeerIngredientsSchema(Schema):
    id = fields.Integer(dump_only=True)
    ingredient_name = fields.String(dump_only=True)
    beer_id = fields.Integer(dump_only=True)

    class Meta:
        strict = True
