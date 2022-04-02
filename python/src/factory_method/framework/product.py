import abc

from ...common.custom_pydantic.model import ABCModel


class ProductABC(ABCModel):
    @abc.abstractmethod
    def use(self) -> None:
        pass
