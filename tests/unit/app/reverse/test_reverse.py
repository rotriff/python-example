import pytest
from app.lists.reverse.reverse import revers


@pytest.mark.parametrize(
    "inp_list, rev_list", [([0, 1, 2, 3, 4], [4, 3, 2, 1, 0]),
                           ([1, 2, 3], [3, 2, 1]),
                           ([1, 2], [2, 1])]
)
def test_reverse(inp_list: list, rev_list: list):
    assert rev_list == revers(inp_list)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, "1, 2 ,3"),
                                           (TypeError, 1),
                                           (TypeError, 1.1)]
)
def test_reverse_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        revers(improper_input)
