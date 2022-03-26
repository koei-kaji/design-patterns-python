from typing import Tuple

from pytest import CaptureFixture


def assert_capture_str(capfd: CaptureFixture[str], expected: Tuple[str, str]) -> None:
    result = capfd.readouterr()
    assert result.out == expected[0]
    assert result.err == expected[1]
