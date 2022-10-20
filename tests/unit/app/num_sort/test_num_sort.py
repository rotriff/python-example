import pytest
from app.lists.num_sort.num_sort import num_sort


@pytest.mark.parametrize(
    "inp_list, sorted_num", [([5, 2, 6, 0], [0, 2, 5, 6]),
                             ([-3, 0, -5, 1], [-5, -3, 0, 1])]
)
def test_num_sort(inp_list: list, sorted_num: list):
    assert sorted_num == num_sort(inp_list)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, "1, 2 ,3"),
                                           (TypeError, 1),
                                           (TypeError, 1.1)]
)
def test_num_sort_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        num_sort(improper_input)
