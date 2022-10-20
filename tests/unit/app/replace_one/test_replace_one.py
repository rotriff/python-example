import pytest
from app.strings.replace_one.replace_one import replace_one


@pytest.mark.parametrize(
    "input_str, one_replaced", [("1", 'one'),
                                ("no one", "no one")]
)
def test_replace_one(input_str: str, one_replaced: str):
    assert one_replaced == replace_one(input_str)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, [1, 2, 3]),
                                           (TypeError, 1),
                                           (TypeError, 1.1),
                                           (TypeError, (1, 2, 3))]
)
def test_replace_one_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        replace_one(improper_input)