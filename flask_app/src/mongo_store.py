from pymongo import MongoClient
from store import KeyValueStore
from config import Config as settings

class MongoDBStore(KeyValueStore):
    def __init__(self) -> None:
        self.client = MongoClient(
        f"mongodb://{settings.mongo_username}:{settings.mongo_password}@db:{settings.mongo_port}/?authSource=admin")
        self.db = self.client[settings.mongo_db]
        self.collection = self.db[settings.collection]

    def create_key_value(self, key: str, value: str) -> None:
        self.collection.insert_one({"key": key, "value": value})

    def update_key_value(self, key: str, value: str) -> None:
        self.collection.update_one({"key": key}, {"$set": {"value": value}})

    def read_key_value(self, key: str) -> str | None:
        result = self.collection.find_one({"key": key})
        if result:
            return result["value"]
        return None

