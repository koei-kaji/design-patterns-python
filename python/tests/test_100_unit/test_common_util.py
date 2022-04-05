from datetime import datetime
from time import sleep
from typing import cast

import pytest

from src.common.util import Class_, ClassNotFoundException


class TestClass_:
    def test_get_class_normal(self) -> None:
        datetime_before = datetime.now()
        sleep(0.1)
        D = cast(datetime, Class_.get_class("datetime.datetime"))
        datetime_target = D.now()
        sleep(0.1)
        datetime_after = datetime.now()

        assert type(datetime_target) is datetime
        assert datetime_before < datetime_target < datetime_after

    def test_get_class_exc(self) -> None:
        # when module not found
        with pytest.raises(ClassNotFoundException):
            Class_.get_class("dummy.nothing")

        # when empty module
        with pytest.raises(ClassNotFoundException):
            Class_.get_class("tests")

        # when module not found inside module
        with pytest.raises(ClassNotFoundException):
            Class_.get_class("tests.nothing")
