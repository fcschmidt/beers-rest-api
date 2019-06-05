import pytest
from beers.tests.utils.populate_data_base import populate_beers
from beers.app.blueprints.api.models.beer_model import Beer
from beers.app.blueprints.api.utils import beers_serializer

from beers.tests.dictionaries.beers_populate_data_test import BEERS_DATA
from beers.tests.dictionaries.beers_data_test import NEW_BEER_DATA


@pytest.mark.usefixtures('session')
class TestBeerModel:

    def test_create_beer(self):
        populate_beers(2)
        get_beer = Beer.get_beer_id(1)
        assert get_beer.id == 1
        assert get_beer.beer_name == BEERS_DATA[0]['beer_name']

    def test_delete_beer(self):
        populate_beers(2)
        query_beer = Beer.get_beer_id(1)
        query_beer.delete()
        get_beer = Beer.get_beer_id(1)
        assert get_beer is None

    def test_update_beer(self):
        populate_beers(2)
        query_beer = Beer.get_beer_id(1)
        Beer.update(query_beer, NEW_BEER_DATA)
        get_beer = Beer.get_beer_id(1)
        assert get_beer.id == 1
        assert get_beer.beer_name == NEW_BEER_DATA['beer_name']

    def test_list_all_beers_empty(self):
        get_all_beers = Beer.get_beers()
        assert len(get_all_beers) == 0

    def test_list_all_beers(self):
        populate_beers(2)
        get_all_beers = Beer.get_beers()
        serialized = beers_serializer(get_all_beers, True)
        assert len(serialized) > 0
        assert serialized[0]['beer_name'] == BEERS_DATA[0]['beer_name']

    def test_filter_beer_by_name(self):
        populate_beers(2)
        beer_name = BEERS_DATA[0]['beer_name']
        query_filter_name = Beer.filter_beer_name(beer_name)
        serialized = beers_serializer(query_filter_name, True)
        assert serialized[0]['id'] == 1
        assert serialized[0]['beer_name'] == BEERS_DATA[0]['beer_name']

    def test_filter_beer_by_color(self):
        populate_beers(2)
        beer_color = BEERS_DATA[0]['color']
        query_filter_color = Beer.filter_beer_color(beer_color)
        serialized = beers_serializer(query_filter_color, True)
        assert serialized[0]['color'] == BEERS_DATA[0]['color']
        assert serialized[0]['beer_name'] == BEERS_DATA[0]['beer_name']

    def test_filter_beer_by_alcohol(self):
        populate_beers(2)
        beer_alcohol = BEERS_DATA[0]['alcohol']
        query_filter_alcohol = Beer.filter_beer_alcohol(beer_alcohol)
        serialized = beers_serializer(query_filter_alcohol, True)
        assert str(serialized[0]['alcohol']) == str(float(BEERS_DATA[0]['alcohol']))
        assert serialized[0]['beer_name'] == BEERS_DATA[0]['beer_name']

    def test_filter_beer_by_temperature(self):
        populate_beers(2)
        beer_temperature = BEERS_DATA[0]['temperature']
        query_filter_temperature = Beer.filter_beer_temperature(beer_temperature)
        serialized = beers_serializer(query_filter_temperature, True)
        assert str(serialized[0]['temperature']) == str(float(BEERS_DATA[0]['temperature']))
        assert serialized[0]['beer_name'] == BEERS_DATA[0]['beer_name']
