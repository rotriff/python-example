import pytest
from app.lists.greatest_num.greatest_nums import greatest_nums


@pytest.mark.parametrize(
    "inp_list, num_ind", [([0, 1, 2, 3, 4], (4, 4)),
                          ([1, 2, 3], (3, 2)),
                          ([1, 2], (2, 1))]
)
def test_greatest_nums(inp_list: list, num_ind: tuple):
    assert num_ind == greatest_nums(inp_list)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, "1, 2 ,3"),
                                           (TypeError, 1),
                                           (TypeError, 1.1)]
)
def test_greatest_nums_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        greatest_nums(improper_input)
