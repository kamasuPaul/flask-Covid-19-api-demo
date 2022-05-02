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
