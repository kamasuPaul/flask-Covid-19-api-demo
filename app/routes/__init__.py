from flask_restful import Api
from app.controllers import (
    IndexView,
    CasesView,
    CountriesView,
    SummaryView
    )

api = Api()

#add endpoint for refreshing data
api.add_resource(CasesView, '/countries/refresh')
api.add_resource(CountriesView,'/countries')
api.add_resource(IndexView, '/')
# Index route
api.add_resource(SummaryView, '/summary')

