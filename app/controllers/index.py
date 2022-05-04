from flask_restful import Resource
from app.models.country import Country
from flask import jsonify
from sqlalchemy.sql import functions

class IndexView(Resource):

    def get(self):
        return dict(status="success", message="Welcome to the API")

class CountriesView(Resource):
    #get all countries
    def get(self):
        countries = Country.find_all();
        data = []
        for country in countries:
            data.append(country.toDict())
        return dict(status="success", message="Countries retrieved successfully", data=data)

class SummaryView(Resource):
    #get totals
    def get(self):
        #get the sum of all cases from sqlalchemy
        result = Country.query.with_entities(
                    functions.sum(Country.deaths).label("total_deaths"),
                    functions.sum(Country.confirmed_cases).label("total_confirmed_cases"),
                    functions.sum(Country.recovered_cases).label("total_recovered_cases"),
                    functions.sum(Country.population).label("total_population")
                ).first()
        dict_data = {
            'total_deaths': result.total_deaths,
            'total_recovered_cases': result.total_recovered_cases,
            'total_confirmed_cases': result.total_confirmed_cases,
            'total_population': result.total_population
        }
        return dict(status="success", message="Succesfull", data=dict_data)
