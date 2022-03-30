# NOTE: https://pydantic-docs.helpmanual.io/usage/model_config/
from pydantic.config import BaseConfig as PydanticBaseConfig


class BaseConfig(PydanticBaseConfig):
    validate_all = True
    validate_assignment = True


class BaseFrozenConfig(BaseConfig):
    validate_all = True
    allow_mutation = False
