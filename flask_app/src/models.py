from dataclasses import dataclass
from typing import TypedDict
from bson import ObjectId


__all__ = ('KeyValueDocument', 'KeyValueData',)


@dataclass
class KeyValueDocument:
    _id: ObjectId
    key: str
    value: str

    def to_dict(self) -> 'KeyValueData':
        return KeyValueData(key=self.key, value=self.value)

class KeyValueData(TypedDict):
    key: str
    value:str


