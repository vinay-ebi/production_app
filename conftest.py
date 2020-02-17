import pytest
from production.test_app import main

# returns our flask app instance
@pytest.fixture
def app():
    app = main()
    return app
