import pytest
from app.lists.even_index.even_index import even_index


@pytest.mark.parametrize(
    "inp_list, even_inxs", [([0, 1, 2, 3, 4], [2, 4]),
                            ([1, 2, 3], [3]),
                            ([1, 2], [])]
)
def test_even_index(inp_list: list, even_inxs: list):
    assert even_inxs == even_index(inp_list)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, "1, 2 ,3"),
                                           (TypeError, 1),
                                           (TypeError, 1.1)]
)
def test_even_index_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        even_index(improper_input)
