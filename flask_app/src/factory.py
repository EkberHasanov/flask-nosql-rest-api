from typing import Optional
from store import KeyValueStore
from mongo_store import MongoDBStore


class KeyValueStoreFactory:
    @staticmethod
    def get_store(store_type: Optional[str] = None) -> KeyValueStore:
        if store_type == "mongo":
            return MongoDBStore()
        else:
            raise ValueError("Invalid store type")


