from typing import Generator, Tuple, Type

import pytest
from py._path.local import LocalPath
from pydantic import BaseConfig
from pytest import CaptureFixture, MonkeyPatch


def assert_capture_str(capfd: CaptureFixture[str], expected: Tuple[str, str]) -> None:
    result = capfd.readouterr()
    assert result.out == expected[0]
    assert result.err == expected[1]


def assert_pydantic_config(
    config_a: Type[BaseConfig], config_b: Type[BaseConfig]
) -> None:
    assert config_a.title == config_b.title
    assert config_a.anystr_lower == config_b.anystr_lower
    assert config_a.anystr_strip_whitespace == config_b.anystr_strip_whitespace
    assert config_a.min_anystr_length == config_b.min_anystr_length
    assert config_a.max_anystr_length == config_b.max_anystr_length
    assert config_a.validate_all == config_b.validate_all
    assert config_a.extra == config_b.extra
    assert config_a.allow_mutation == config_b.allow_mutation
    assert config_a.frozen == config_b.frozen
    assert (
        config_a.allow_population_by_field_name
        == config_b.allow_population_by_field_name
    )
    assert config_a.use_enum_values == config_b.use_enum_values
    assert config_a.fields == config_b.fields
    assert config_a.validate_assignment == config_b.validate_assignment
    assert config_a.error_msg_templates == config_b.error_msg_templates
    assert config_a.arbitrary_types_allowed == config_b.arbitrary_types_allowed
    assert config_a.orm_mode == config_b.orm_mode
    assert config_a.getter_dict == config_b.getter_dict
    assert config_a.alias_generator == config_b.alias_generator
    assert config_a.keep_untouched == config_b.keep_untouched
    assert config_a.schema_extra == config_b.schema_extra
    assert config_a.json_loads == config_b.json_loads
    assert config_a.json_dumps == config_b.json_dumps
    assert config_a.json_encoders == config_b.json_encoders
    assert (
        config_a.underscore_attrs_are_private == config_b.underscore_attrs_are_private
    )
    assert config_a.copy_on_model_validation == config_b.copy_on_model_validation
    assert config_a.smart_union == config_b.smart_union


@pytest.fixture(scope="function")
def chdir_to_tmpdir(
    tmpdir: LocalPath, monkeypatch: MonkeyPatch
) -> Generator[None, None, None]:
    monkeypatch.chdir(tmpdir)
    yield
