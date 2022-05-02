from flask_restful import Resource
import requests
from app.models.country import Country

class CasesView(Resource):
    #fetches data from the api and refresh the database
    def get(self):
        self.fetchData()
        return dict(status="success", message="Refreshing data")


    def fetchData(self):
        #call the api and get the data
        data = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
        data = data.json()
        #loop through the data and insert into the database
        for key , value in data.items():
            country_data = value['All']
            #insert into the database
            self.insertData(country_data,key)

    def insertData(self, item, country_name):
        #init country object
        country = Country(
            name=country_name,
            confirmed_cases=item.get('confirmed'),
            deaths=item.get('deaths',0),
            recovered_cases=item.get('recovered',0),
            population=item.get('population',0),
            continent=item.get('continent',''),
            abbreviation=item.get('abbreviation',''),
            location=item.get('location',''),
            iso=item.get('iso',''),
            capital_city=item.get('capital_city', None),
            lat=item.get('lat', None),
            long=item.get('long',None),
            last_updated_at=item.get('updated', None),
            sq_km_area=item.get('sq_km_area', None)
        )
        country.save()
        

