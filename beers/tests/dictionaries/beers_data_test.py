NEW_BEER_DATA = {
    'beer_name': 'Skoll',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'color': 'clara',
    'alcohol': 3.0,
    'temperature': 4.0,
    'ingredients': [
        {'names': ['cevada', 'lupulo', 'malte', 'trigo']}
    ]
}

UPDATE_BEER_DATA = {
    'beer_name': 'Adriática',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'color': 'clara',
    'alcohol': 5,
    'temperature': 5.0,
    'ingredients': {
        'list': [
            {'ingredient_name': 'cevada', 'id': 1},
            {'ingredient_name': 'lupulo', 'id': 2},
            {'ingredient_name': 'malte', 'id': 3},
        ]
    }
}

UPDATE_BEER_NOT_EXIST = {
    'beer_name': 'Skoll',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'color': 'clara',
    'alcohol': 3.0,
    'temperature': 4.0,
    'ingredients': {
        'list': [
            {'ingredient_name': 'cevada', 'id': 1},
            {'ingredient_name': 'lupulo', 'id': 2},
            {'ingredient_name': 'malte', 'id': 3},
        ]
    }
}

UPDATE_BEER_NOT_EXIST_INGREDIENT = {
    'beer_name': 'Skoll',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'harmonization': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.',
    'color': 'clara',
    'alcohol': 3,
    'temperature': 4.0,
    'ingredients': {
        'list': [
            {'ingredient_name': 'cevada', 'id': 55},
            {'ingredient_name': 'lupulo', 'id': 100},
            {'ingredient_name': 'malte', 'id': 49},
        ]
    }
}