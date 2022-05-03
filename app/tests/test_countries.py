#define class
class TestCountries:
    #define setup
    def setup(self):
        from server import create_app
        from app.models import db
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = db
        self.db.create_all()
        self.db.session.commit()
    #define teardown
    def teardown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()
    #test refresh
    def test_refresh_route_returns_200(self):
        response = self.client.get('countries/refresh')
        assert response.status_code == 200
    #test get all countries returns 200
    def test_get_all_countries_returns_200(self):
        response = self.client.get('countries')
        assert response.status_code == 200
        
    #test get all countries returns json
    def test_get_all_countries_returns_json(self):
        response = self.client.get('countries')
        assert response.content_type == 'application/json'

    #test get all countries returns correct data
    def test_get_all_countries_returns_correct_data(self):
        response = self.client.get('countries')
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Countries retrieved successfully'
        assert response.json['data'] == []


