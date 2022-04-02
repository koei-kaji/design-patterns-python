# NOTE: https://pydantic-docs.helpmanual.io/usage/model_config/
from pydantic.config import BaseConfig as PydanticBaseConfig


class ABCConfig(PydanticBaseConfig):
    copy_on_model_validation = False


class BaseConfig(PydanticBaseConfig):
    validate_all = True
    validate_assignment = True
    copy_on_model_validation = False


class BaseFrozenConfig(PydanticBaseConfig):
    validate_all = True
    allow_mutation = False
    copy_on_model_validation = False
