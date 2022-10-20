import pytest
from app.strings.h_delete.h_delete import h_delete


@pytest.mark.parametrize(
    "input_h_string, h_deleted", [("Hello there", "ere"),
                                  ("hello", "ello"),
                                  ("no deletion", "no deletion")]
)
def test_h_delete(input_h_string: str, h_deleted: str):
    assert h_deleted == h_delete(input_h_string)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, [1, 2, 3]),
                                           (TypeError, 1),
                                           (TypeError, 1.1),
                                           (TypeError, (1, 2, 3))]
)
def test_h_delete_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        h_delete(improper_input)
