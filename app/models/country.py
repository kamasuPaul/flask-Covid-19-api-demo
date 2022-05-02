from ..models import db
from app.models.root_model import RootModel


class Country(RootModel):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String()) # name of the country
    confirmed_cases = db.Column(db.Integer) # No of confirmed covid cases
    recovered_cases = db.Column(db.Integer)#No of recovered covid cases
    deaths = db.Column(db.Integer)
    population = db.Column(db.Integer)
    sq_km_area = db.Column(db.Integer)
    continent = db.Column(db.String())
    abbreviation = db.Column(db.String())
    location = db.Column(db.String())
    iso = db.Column(db.Integer)
    capital_city = db.Column(db.String())
    lat = db.Column(db.String())
    long = db.Column(db.String())
    last_updated_at = db.Column(db.String())

    def __init__(self, name, confirmed_cases, recovered_cases, deaths, population, sq_km_area, continent, abbreviation, location, iso, capital_city, lat, long, last_updated_at):
        self.name = name
        self.confirmed_cases = confirmed_cases
        self.recovered_cases = recovered_cases
        self.deaths = deaths
        self.population = population
        self.sq_km_area = sq_km_area
        self.continent = continent
        self.abbreviation = abbreviation
        self.location = location
        self.iso = iso
        self.capital_city = capital_city
        self.lat = lat
        self.long = long
        self.last_updated_at = last_updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
