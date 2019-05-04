.PHONY: test install pep8 clean

DB_NAME=beers

test:
	@echo 'Run coverage and starting tests'
	@pytest --verbose --cov=app --color=yes tests/

report:
	@echo 'Report coverage and generate html'
	coverage report
	coverage html -d coverage_html


install:
	@echo 'Create environment and Instal dependences'
	@virtualenv -p python3.6 .venv
	@source .venv/bin/activate
	@pip install --upgrade pip
	@pip install -r requirements.txt

migrate:
	@echo 'Created Migrations'
	flask db init
	flask db migrate -m "Created Migrations."
	flask db upgrade

createdb:
	@echo 'Create Data base (PostgreSQL Data Base)'
	createdb $(DB_NAME)
	@echo 'Data Base $(DB_NAME) Create Successfully'

dropdb:
	@echo 'Drop Data base'
	dropdb $(DB_NAME)
	@echo 'Data Base $(DB_NAME) Delete Successfully'

run:
	@echo 'Start application'
	flask run

clean:
	rm -rf migrations .coverage coverage_html .pytest_cache