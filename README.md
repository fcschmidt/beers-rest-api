# :beers: RestAPI 

`Documentation In Progress.`

## Preparing the Environment


## Generating Migrations


## Run application


## RestAPI Resources


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
    "description": "A Cerveja Adriática 600ml foi criada pelo alemão Henrique Thielen, um visionário cervejeiro do início do século XX, ela teve seu nome em homenagem a cervejaria que traduz toda uma era de tradição passada de pai para filho. Hoje, conhecida como a irmã mais velha da Original, ela é uma cerveja pedida certa para a mesa de bar. Reconhecidamente uma cerveja puro malte de alta qualidade, fácil de beber e com aromas especiais que dão um toque equilibrado!.",
    "harmonization": "Ela é leve e refrescante, por isso harmoniza muito bem com pratos leves! Assim, um sabor não vai sobrepor o outro!",
    "color": "clara",
    "alcohol": "3",
    "temperature": "0",
    "ingredients": [
        {"names": ["cevada", "lupulo", "malte", "trigo"]}
    ]
}
```

**Update:**

```json
{
    "beer_name": "Skoll",
    "description": "A Cerveja Adriática 600ml foi criada pelo alemão Henrique Thielen, um visionário cervejeiro do início do século XX, ela teve seu nome em homenagem a cervejaria que traduz toda uma era de tradição passada de pai para filho. Hoje, conhecida como a irmã mais velha da Original, ela é uma cerveja pedida certa para a mesa de bar. Reconhecidamente uma cerveja puro malte de alta qualidade, fácil de beber e com aromas especiais que dão um toque equilibrado!.",
    "harmonization": "Ela é leve e refrescante, por isso harmoniza muito bem com pratos leves! Assim, um sabor não vai sobrepor o outro!",
    "color": "clara",
    "alcohol": "3",
    "temperature": "0",
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
|GET|`http://localhost:5000/api/v1/beers`|200||
|GET|`http://localhost:5000/api/v1/beers?beer_name=<string>`|200||
|GET|`http://localhost:5000/api/v1/beers?color=<string>`|200||
|GET|`http://localhost:5000/api/v1/beers?alcohol=<string>`|200||
|GET|`http://localhost:5000/api/v1/beers?temperature=<string>`|200||
|GET|`http://localhost:5000/api/v1/beers?ingredient=<string>`|200||


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
GNU AFFERO GENERAL PUBLIC LICENSE 3
