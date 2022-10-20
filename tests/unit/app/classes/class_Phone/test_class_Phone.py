import pytest
from app.classes.class_Phone.class_Phone import Phone


@pytest.fixture
def my_phone():
    phone = Phone("0675553535", "Phone", 100)
    return phone


@pytest.mark.parametrize(
    "caller_name, maybe_number, screen_message", [("Someone", "0123",
                                                   f'Someone is calling on Phone with number 0123'),
                                                  ("No_name", None, "No_name is calling on Phone")]
)
def test_receive_call(my_phone, caller_name: str, maybe_number: str, screen_message: str):
    assert screen_message == my_phone.receive_call(caller_name, maybe_number)


@pytest.mark.parametrize(
    "expected_exception, improper_name, improper_number", [(TypeError, 1010, 1.2),
                                                           (TypeError, 1.2, None)]
)
def test_receive_call_exception(my_phone, expected_exception, improper_name, improper_number):
    with pytest.raises(expected_exception):
        my_phone.receive_call(improper_name, improper_number)


@pytest.mark.parametrize(
    "recipient_number, message_of_numbers", [(("01324",), "Phone sends message on the following number(s): ('01324',)"),
                                             (("111", "222"),
                                              "Phone sends message on the following number(s): ('111', '222')")]
)
def test_send_message(my_phone, recipient_number: str, message_of_numbers: str):
    assert message_of_numbers == my_phone.send_message(*recipient_number)


@pytest.mark.parametrize(
    "expected_exception, improper_numbers", [(TypeError, (1010, )),
                                             (TypeError, (1.2, 1010))]
)
def test_send_message_exception(my_phone, expected_exception, improper_numbers):
    with pytest.raises(expected_exception):
        my_phone.send_message(*improper_numbers)


def test_get_number(my_phone):
    assert "0675553535" == my_phone.get_number()


@pytest.fixture
def wrong_number_phone():
    phone_wn = Phone(6755535, "Phone", 100)
    return phone_wn


@pytest.fixture
def wrong_model_phone():
    phone_wm = Phone("6755535", 100, 100)
    return phone_wm


@pytest.fixture
def wrong_weight_phone():
    phone_ww = Phone("6755535", "Phone", "100")
    return phone_ww


@pytest.fixture
def wrong_empty_phone():
    phone_we = Phone(None, None, None)
    return phone_we


'''
@pytest.mark.parametrize(
    "expected_exception, improper_object", [(TypeError, wrong_number_phone),
                                            (TypeError, wrong_model_phone),
                                            (TypeError, wrong_weight_phone),
                                            (ValueError, wrong_empty_phone)]
)
def test_get_number_exception(expected_exception, improper_object):
    with pytest.raises(expected_exception):
        improper_object.get_number()
'''


def test_get_number_wn_exception(wrong_number_phone):
    with pytest.raises(TypeError):
        wrong_number_phone.get_number()


def test_get_number_wm_exception(wrong_model_phone):
    with pytest.raises(TypeError):
        wrong_model_phone.get_number()


def test_get_number_ww_exception(wrong_weight_phone):
    with pytest.raises(TypeError):
        wrong_weight_phone.get_number()


def test_get_number_we_exception(wrong_empty_phone):
    with pytest.raises(TypeError):
        wrong_empty_phone.get_number()
