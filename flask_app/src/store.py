from abc import ABC, abstractmethod


class KeyValueStore(ABC):
    @abstractmethod
    def create_key_value(self, key: str, value: str) -> None:
        ...

    @abstractmethod
    def update_key_value(self, key: str, value: str) -> None:
        ...

    @abstractmethod
    def read_key_value(self, key: str) -> str:
        ...

