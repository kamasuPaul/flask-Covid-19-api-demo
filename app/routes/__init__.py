from flask_restful import Api
from app.controllers import (
    IndexView,
    CasesView
    )

api = Api()

#add endpoint for refreshing data
api.add_resource(CasesView, '/countries/refresh')
# Index route
api.add_resource(IndexView, '/')

