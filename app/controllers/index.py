from flask_restful import Resource
from app.models.country import Country
from flask import jsonify


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
