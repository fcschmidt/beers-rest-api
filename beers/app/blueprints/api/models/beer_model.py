from beers.app.ext.db import db


class Beer(db.Model):
    """Beers Model"""
    __tablename__ = 'beers'

    id = db.Column(db.Integer, primary_key=True)
    beer_name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    harmonization = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(40), nullable=False)
    alcohol = db.Column(db.String(40), nullable=False)
    temperature = db.Column(db.String(40), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update(beer, data):
        beer.beer_name = data['beer_name']
        beer.description = data['description']
        beer.harmonization = data['harmonization']
        beer.color = data['color']
        beer.alcohol = data['alcohol']
        beer.temperature = data['temperature']
        db.session.commit()

    @staticmethod
    def get_beers():
        return Beer.query.all()

    @staticmethod
    def get_beer_id(beer_id):
        return Beer.query.get(beer_id)

    @staticmethod
    def filter_beer_name(beer_name):
        return Beer.query.filter(Beer.beer_name == beer_name).all()

    @staticmethod
    def filter_beer_color(color):
        return Beer.query.filter(Beer.color == color).all()

    @staticmethod
    def filter_beer_alcohol(alcohol):
        return Beer.query.filter(Beer.alcohol == alcohol).all()

    @staticmethod
    def filter_beer_temperature(temperature):
        return Beer.query.filter(Beer.temperature == temperature).all()

    def __repr__(self):
        return f'beers(id={self.id}, beer_name={self.beer_name}, description={self.description},' \
            f'harmonization={self.harmonization}, color={self.color}, alcohol={self.alcohol},' \
            f'temperature={self.temperature}'

