import pytest
from app.lists.even_els.even_els import even_els


@pytest.mark.parametrize(
    "inp_list, evens", [([0, 1, 2, 3, 4], [2, 4]),
                        ([1, 2, 3], [2]),
                        ([1, 2], [2])]
)
def test_even_els(inp_list: list, evens: list):
    assert evens == even_els(inp_list)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, "1, 2 ,3"),
                                           (TypeError, 1),
                                           (TypeError, 1.1)]
)
def test_even_els_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        even_els(improper_input)
