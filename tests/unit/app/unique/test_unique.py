import pytest
from app.lists.unique.unique import unique


@pytest.mark.parametrize(
    "inp_list, uniq_list", [([1, 1, 2, 3, 3], [2]),
                            ([1, 2, 3], [1, 2, 3]),
                            ([2, 2, 2], [])]
)
def test_unique(inp_list: list, uniq_list: list):
    assert uniq_list == unique(inp_list)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, "1, 2 ,3"),
                                           (TypeError, 1),
                                           (TypeError, 1.1)]
)
def test_unique_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        unique(improper_input)