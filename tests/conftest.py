import pytest
from pymongo_inmemory import MongoClient
from fastapi.testclient import TestClient

from app.data.database.database import MongoBase
from mock import patch

from app.main import app


@pytest.fixture(scope="session")
def test_mongo_db_client():
    mongo_client = MongoClient()
    with patch.object(MongoBase, '_client', mongo_client):
        yield mongo_client

    mongo_client.close()


@pytest.fixture(autouse=True)
def test_mongo_db(test_mongo_db_client):

    test_mongo_db = MongoBase.database
    yield MongoBase.database

    test_mongo_db.command("dropDatabase")


@pytest.fixture(autouse=True)
def test_app():
    return app


@pytest.fixture
def test_client(test_app):
    return TestClient(test_app)

