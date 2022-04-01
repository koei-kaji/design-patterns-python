from typing import Dict

from pydantic import BaseModel, PrivateAttr

from .product import ProductABC


class Manager(BaseModel):
    _showcase: Dict[str, ProductABC] = PrivateAttr(default={})

    def register(self, name: str, proto: ProductABC) -> None:
        self._showcase[name] = proto

    def create(self, proto_name: str) -> ProductABC:
        product = self._showcase[proto_name]
        return product.create_clone()
