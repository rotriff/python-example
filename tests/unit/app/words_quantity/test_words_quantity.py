import pytest
from app.strings.words_quantity.words_quantity import words_quantity


@pytest.mark.parametrize(
    "input_str, quantity", [("Hello world", 2),
                            ("1 2 3 4 5", 5),
                            ("Text", 1)]
)
def test_words_quantity(input_str: str, quantity: int):
    assert quantity == words_quantity(input_str)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, [1, 2, 3]),
                                           (TypeError, 1),
                                           (TypeError, 1.1),
                                           (TypeError, (1, 2, 3))]
)
def test_words_quantity_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        words_quantity(improper_input)