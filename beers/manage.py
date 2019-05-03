from os import getenv
from beers.app.app_factory import create_app

app = create_app(getenv('FLASK_ENV') or 'default')
