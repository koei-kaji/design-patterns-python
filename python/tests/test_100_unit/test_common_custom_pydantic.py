import pytest
from pydantic import (
    BaseModel,
    PrivateAttr,
    StrictBool,
    StrictInt,
    StrictStr,
    ValidationError,
)

from src.common.custom_pydantic.config import ABCConfig, BaseConfig, BaseFrozenConfig
from tests.conftest import assert_pydantic_config


class SubDummyModel(BaseModel):
    prop_str: StrictStr = "sub"


class SubDummyModelWithABCConfig(SubDummyModel):
    class Config(ABCConfig):
        pass


class DummyModel(BaseModel):
    prop_str: StrictStr = "string"
    prop_int: StrictInt = 999
    prop_bool: StrictBool = True
    _prop_private_str: str = PrivateAttr(default="private")


class DummyModelAddedSubDummyModel(DummyModel):
    sub: SubDummyModel = SubDummyModel()


class DummyModelAddedSubDummyModelWithABCConfig(DummyModel):
    sub: SubDummyModelWithABCConfig = SubDummyModelWithABCConfig()


class InvalidDefaultDummyModel(BaseModel):
    prop_str: StrictStr = 999  # type: ignore
    prop_int: StrictInt = "999"  # type: ignore
    prop_bool: StrictBool = "True"  # type: ignore


class DummyModelWithBaseConfig(DummyModel):
    class Config(BaseConfig):
        pass


class InvalidDefaultDummyModelWithBaseConfig(InvalidDefaultDummyModel):
    class Config(BaseConfig):
        pass


class DummyModelWithBaseFrozenConfig(DummyModel):
    class Config(BaseFrozenConfig):
        pass


class InvalidDefaultDummyModelWithBaseFrozenConfig(InvalidDefaultDummyModel):
    class Config(BaseFrozenConfig):
        pass


class TestPydanticBaseConfig:
    def test_validate_assignment_false(self) -> None:
        # インスタンス生成時には型チェックが行われる
        with pytest.raises(ValidationError):
            DummyModel(prop_str=999)

        # 最初の一回以外、型チェックが行われない
        updated_value = 999
        model = DummyModel()
        model.prop_str = updated_value  # type:ignore
        assert model.prop_str == updated_value  # type: ignore

    def test_validate_all_false(self) -> None:
        # 初期値のチェックが行われない
        InvalidDefaultDummyModel()
        assert True

    def test_allow_mutation_true(self) -> None:
        # インスタンス化生成以降も値の変更を許容する
        updated_str = "update"
        model = DummyModel()
        model.prop_str = updated_str
        assert model.prop_str == updated_str

    def test_copy_on_model_validation_true(self) -> None:
        # ネストされるモデルは再構築される
        sub = SubDummyModel()
        model = DummyModelAddedSubDummyModel(sub=sub)
        assert id(sub) != id(model.sub)


class TestABCConfig:
    def test_config(self) -> None:
        model = SubDummyModelWithABCConfig()
        assert_pydantic_config(model.Config, ABCConfig)

    def test_copy_on_model_validation_false(self) -> None:
        # ネストされるモデルは再構築されない
        sub = SubDummyModelWithABCConfig()
        model = DummyModelAddedSubDummyModelWithABCConfig(sub=sub)
        assert id(sub) == id(model.sub)


class TestBaseConfig:
    def test_config(self) -> None:
        model = DummyModelWithBaseConfig()
        assert_pydantic_config(model.Config, BaseConfig)

    def test_validate_assignment_true(self) -> None:
        # インスタンス化時には型チェックは行われる
        with pytest.raises(ValidationError):
            DummyModelWithBaseConfig(prop_str=999)

        # 最初の一回以外にも型チェックを行う
        model = DummyModelWithBaseConfig()
        with pytest.raises(ValidationError):
            model.prop_str = 999  # type:ignore

    def test_validate_all_true(self) -> None:
        # 初期値のチェックを行う
        with pytest.raises(ValidationError):
            InvalidDefaultDummyModelWithBaseConfig()


class TestBaseFrozenConfig:
    def test_config(self) -> None:
        model = DummyModelWithBaseFrozenConfig
        assert_pydantic_config(model.Config, BaseFrozenConfig)

    def test_validate_all_true(self) -> None:
        # 初期値のチェックを行う
        with pytest.raises(ValidationError):
            InvalidDefaultDummyModelWithBaseFrozenConfig()

    def test_allow_mutation_true(self) -> None:
        # インスタンス化生成以降も値の変更を許容する
        model = DummyModelWithBaseFrozenConfig()
        with pytest.raises(TypeError):
            model.prop_str = "update"
