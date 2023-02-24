
__all__ = ("Config",)


class Config(object):
    mongo_host: str = 'localhost'
    mongo_port: int = 27017
    mongo_db: str = 'db'
    collection: str = 'key_value'
    mongo_username: str = 'root'
    mongo_password: str = '1234'
    store_type: str = 'mongo'


