import logging
from typing import Optional
from flask import Flask, jsonify, request
from db import client
from bson import ObjectId
from config import Config as settings
from models import KeyValueData
from factory import KeyValueStoreFactory
from store import KeyValueStore

__all__ = ('app', )


logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s]: %(message)s',
        handlers=[logging.StreamHandler()]
    )
logger = logging.getLogger(__name__)


app = Flask(__name__)
store: KeyValueStore = KeyValueStoreFactory.get_store(store_type=settings.store_type)


@app.route("/read/<key>", methods=["GET"])
def read(key: str) -> str:
    value = store.read_key_value(key=key)
    if value:
        return jsonify({"key": key, "value": value})
    else:
        return jsonify({'message': 'Key not found'})

@app.route("/create", methods=["POST"])
def create() -> str:
    try:
        data = request.json
        store.create_key_value(key=data["key"], value=data["value"])
        return jsonify({'message': 'Created successfully'})
    except Exception as error:
        logger.info(error)
        return jsonify({'message': 'Internal server error'})

@app.route("/update/<key>", methods=["PUT"])
def update(key: str) -> str:
    data = request.get_json()
    new_value = data['value']
    store.update_key_value(key=key, value=new_value)
    return jsonify({'message': f'updated key ({key}: {new_value})'})

