# :beers: RestAPI


## Preparing the Environment

**Clone the project**

`$ git clone git@github.com:fcschmidt/beers-rest-api.git`

**Enter the project**

`$ cd beers-rest-api/`

**Create a file `.env`**

```bash
export FLASK_APP=manage.py
export FLASK_ENV=development
DEBUG=True
DATABASE_URL='dialect+driver://username:password@host:port/database'
```

About SQLAlchemy Configuration: [https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls](https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls).

If the path DATABASE_URL is not inserted in the .env file. By default it will create a database using SQLite, on the path `sqlite:////var/tmp/beers_dev.sqlite`.

**Creating an isolated development environment with [virtualenv](https://virtualenv.pypa.io/en/latest/) or [pipenv](https://pipenv.readthedocs.io/en/latest/).**

`~/beers-rest-api$ virtualenv -p python3.6 .venv`.


**Activating the environment:**

`~/beers-rest-api$ source .venv/bin/activate.`

**Installing System Dependencies:**

`~/beers-rest-api$ pip install -r requirements.txt.`

## Generating Migrations

```bash
flask db init
flask db migrate -m "Created Meeting Room"
flask db upgrade
```

## Run application

`~/beers-rest-api$ flask run`.

View application in [http://localhost:5000](http://localhost:5000/).


## RestAPI Resources

Methods of accessing resources.

Using [curl](https://curl.haxx.se/).

Python script using [requests](http://docs.python-requests.org/en/master/) lib.

Application for test API [Postman](http://docs.python-requests.org/en/master/) or [Insomnia](https://insomnia.rest/?utm_content=bufferd23bb&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer).

### Beers API

Create, update and delete beer.

|Method|URI|Status Code|Response|
|-------|-------|-------|-------|
|POST|`http://localhost:5000/api/v1/beers`|201|Beer create successfully!|
|PUT|`http://localhost:5000/api/v1/beers/<int:beer_id>`|200|Beer update successfully!|
|DELETE|`http://localhost:5000/api/v1/beers/<int:beer_id>`|202|Beer delete successfully!|


#### Payloads

**Post:**

```json
{
    "beer_name": "Skoll",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.",
    "harmonization": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.",
    "color": "clara",
    "alcohol": 3,
    "temperature": 0,
    "ingredients": [
        {"names": ["cevada", "lupulo", "malte", "trigo"]}
    ]
}
```

**Update:**

```json
{
    "beer_name": "Skoll",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.",
    "harmonization": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius quis ante nec.",
    "color": "clara",
    "alcohol": 3,
    "temperature": 0,
    "ingredients": {
        "list": [
            {"ingredient_name": "cevada", "id": 1},
            {"ingredient_name": "lupulo", "id": 2},
            {"ingredient_name": "malte", "id": 3},
        ]
    }
}
```


### Beers List and Filter API

List all beer to catalog and filter by beer name, beer color, alcohol, temperature or ingrediente name.


|Method|URI|Status Code|Response|
|-------|-------|-------|-------|
|GET|`http://localhost:5000/api/v1/beers`|200|Return [json] all beers|
|GET|`http://localhost:5000/api/v1/beers?beer_name=<string>`|200|Return [json] filter beer by beer name.|
|GET|`http://localhost:5000/api/v1/beers?color=<string>`|200|Return [json], filter beer by color.|
|GET|`http://localhost:5000/api/v1/beers?alcohol=<string>`|200|Return [json] filter beer by alcohol.|
|GET|`http://localhost:5000/api/v1/beers?temperature=<string>`|200|Return [json] filter beer by temperature.|
|GET|`http://localhost:5000/api/v1/beers?ingredient=<string>`|200|Return [json] filter beer by ingredient.|


### Ingredients API

Create and delete ingredients.

|Method|URI|Status Code|Response|
|-------|-------|-------|-------|
|POST|`http://localhost:5000/api/v1/ingredients`|201|Ingredients create successfully!|
|PUT|`http://localhost:5000/api/v1/ingredients`|200|Ingredients update successfully!|
|DELETE|`http://localhost:5000/api/v1/ingredients/<int:ingredient_id>`|202|Ingredients delete successfully!|


#### Payloads


## Test Coverage

|Module|Coverage|
|-------|-------|
|app/app_factory.py|100%|
|app/blueprints/api/beers/resource.py|100%|
|app/blueprints/api/beers_list/resource.py|100%|
|app/blueprints/api/ingredients/resource.py|100%|
|app/blueprints/api/models/beer_model.py|100%|
|app/blueprints/api/models/ingredients_model.py|100%|
|app/blueprints/api/responses.py|100%|
|app/blueprints/api/errors.py|100%|
|app/blueprints/api/schemas.py|100%|
|app/blueprints/api/utils.py|100%|


## License
[GNU Affero General Public License v3](https://www.gnu.org/licenses/agpl-3.0.en.html)
