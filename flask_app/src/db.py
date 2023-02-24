from pymongo import MongoClient
from config import Config as settings

__all__ = ("client",)

client = MongoClient(f"mongodb://{settings.mongo_username}:{settings.mongo_password}@{settings.mongo_host}:{settings.mongo_port}/?authSource=admin")

