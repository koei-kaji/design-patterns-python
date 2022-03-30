import abc
from typing import final

from pydantic import BaseModel

from .product import ProductABC


class FactoryABC(BaseModel, abc.ABC):
    @final
    def create(self, owner: str) -> ProductABC:
        product: ProductABC = self.create_product(owner)
        self.register_product(product)
        return product

    @abc.abstractmethod
    def create_product(self, owner: str) -> ProductABC:
        pass

    @abc.abstractmethod
    def register_product(self, product: ProductABC) -> None:
        pass
