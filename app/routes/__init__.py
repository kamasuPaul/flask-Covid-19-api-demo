from flask_restful import Api
from app.controllers import (
    IndexView,
    CasesView,
    CountriesView
    )

api = Api()

#add endpoint for refreshing data
api.add_resource(CasesView, '/countries/refresh')
api.add_resource(CountriesView,'/countries')
# Index route
api.add_resource(IndexView, '/')

