import pytest
from application import create_app


class TestApplication():
    @pytest.fixture
    def client(self):
        app = create_app('config.DevConfig')
        # yield app.test_client()
        return app.test_client()

    def test_get_tasks(self, client):
        respose = client.get('/api/tasks')
        assert respose.status_code == 200
