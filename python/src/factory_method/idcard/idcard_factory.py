from typing import List, cast

from pydantic import PrivateAttr

from ...common.custom_pydantic.config import BaseConfig
from ..framework.factory import FactoryABC
from ..framework.product import ProductABC
from .idcard import IDCard, IDCardWithSerial


class IDCardFactory(FactoryABC):
    _owners: List[IDCard] = PrivateAttr(default=[])

    def create_product(self, owner: str) -> ProductABC:
        return IDCard(owner=owner)

    def register_product(self, product: ProductABC) -> None:
        self._owners.append(cast(IDCard, product))

    def get_owners(self) -> List[IDCard]:
        return self._owners

    class Config(FactoryABC.Config, BaseConfig):
        pass


class IDCardWithSerialFactory(FactoryABC):
    _owners: List[IDCard] = PrivateAttr(default=[])
    _serial: int = PrivateAttr(default=100)

    def create_product(self, owner: str) -> ProductABC:
        product = IDCardWithSerial(owner=owner, serial=self._serial)
        self._serial += 1
        return product

    def register_product(self, product: ProductABC) -> None:
        self._owners.append(cast(IDCard, product))

    def get_owners(self) -> List[IDCard]:
        return self._owners

    class Config(FactoryABC.Config, BaseConfig):
        pass
