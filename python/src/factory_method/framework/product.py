import abc

from pydantic import BaseModel


class ProductABC(BaseModel, abc.ABC):
    @abc.abstractmethod
    def use(self) -> None:
        pass
