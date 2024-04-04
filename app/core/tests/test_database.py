import pytest
from app.core.database import MongoDb


class TestMongoDb:
    collection = "test"

    @pytest.fixture()
    def data(self):
        return {"name": "test"}

    @pytest.fixture()
    def document(self, data):
        return MongoDb.insert(self.collection, data)

    def test_ping_database(self):
        assert MongoDb.ping() is True

    def test_insert(self, data):
        result = MongoDb.insert(self.collection, data)
        assert result.get("name") == data.get("name")
        MongoDb.delete(self.collection, _id=result.get("id"))

    def test_find(self, document, data):
        result = MongoDb.find(self.collection, _id=document.get("id"))
        assert result.get("name") == data.get("name")
        MongoDb.delete(self.collection, _id=result.get("id"))

    def test_update(self, document):
        new_values = {"name": "test_update"}
        result = MongoDb.update(
            self.collection, {"name": "test_update"}, _id=document.get("id")
        )
        assert result.get("name") == new_values.get("name")
        MongoDb.delete(self.collection, _id=result.get("id"))

    def test_delete(self, document):
        assert MongoDb.delete(self.collection, _id=document.get("id")) is True

    def test_delete_all(self):
        assert MongoDb.delete_all(self.collection) is True
