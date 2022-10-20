import pytest
from app.classes.class_Library.class_Library import Book
from app.classes.class_Library.class_Library import Person
from app.classes.class_Library.class_Library import Reader
from app.classes.class_Library.class_Library import Library


@pytest.fixture
def some_book():
    book = Book("genre1", "title1", "author1")
    return book


@pytest.fixture
def some_person():
    person = Person("name2", "02.02.2002", "2222")
    return person


@pytest.fixture
def some_reader(some_book):
    reader = Reader("name1", 1, "01.01.2001", "1111", [some_book])
    return reader


@pytest.fixture
def some_library(some_reader, some_book):
    library = Library("address1", "library_phone1", [some_book], [some_reader])
    return library


'''
@pytest.mark.parametrize(
    "expected_reader, expected_book, message", [(some_reader, some_book, "name1 took title1")]
)
def test_take_book(some_library, expected_reader: Reader, expected_book: Book, message: str):
    assert message == some_library.take_book(expected_reader, expected_book)
'''


@pytest.mark.parametrize(
    "expected_reader, expected_book, message", [(Reader("name1", 1, "01.01.2001", "1111", []),
                                                 Book("genre1", "title1", "author1"), "name1 took title1"),
                                                (Reader("name2", 2, "02.02.2002", "2222", []),
                                                 Book("genre1", "title1", "author1"), "name2 is not member of library"),
                                                (Reader("name1", 1, "01.01.2001", "1111", []),
                                                 Book("genre2", "title2", "author2"), "title2 unavailable")
                                                ]
)
def test_take_book(some_library, expected_reader: Reader, expected_book: Book, message: str):
    assert message == some_library.take_book(expected_reader, expected_book)


@pytest.mark.parametrize(
    "wrong_reader, wrong_book, expected_exception", [(1, Book("genre1", "title1", "author1"), TypeError),
                                                     (1.1, Book("genre1", "title1", "author1"), TypeError),
                                                     ("reader", Book("genre1", "title1", "author1"), TypeError),
                                                     (Reader("name1", 1, "01.01.2001", "1111", []), 1, TypeError),
                                                     (Reader("name1", 1, "01.01.2001", "1111", []), 1.1, TypeError),
                                                     (Reader("name1", 1, "01.01.2001", "1111", []), 'book', TypeError)]
)
def test_take_book_exception(some_library, wrong_reader, wrong_book, expected_exception):
    with pytest.raises(expected_exception):
        some_library.take_book(wrong_reader, wrong_book)


@pytest.mark.parametrize(
    "expected_reader, expected_book, message", [(Reader("name1", 1, "01.01.2001", "1111",
                                                [Book("genre1", "title1", "author1")]),
                                                 Book("genre1", "title1", "author1"), "name1 returned title1"),
                                                (Reader("name2", 2, "02.02.2002", "2222", []),
                                                 Book("genre1", "title1", "author1"), "name2 is not member of library"),
                                                (Reader("name1", 1, "01.01.2001", "1111", []),
                                                 Book("genre2", "title2", "author2"), "title2 unavailable")
                                                ]
)
def test_return_book(some_library, expected_reader: Reader, expected_book: Book, message: str):
    assert message == some_library.return_book(expected_reader, expected_book)


@pytest.mark.parametrize(
    "wrong_reader, wrong_book, expected_exception", [(1, Book("genre1", "title1", "author1"), TypeError),
                                                     (1.1, Book("genre1", "title1", "author1"), TypeError),
                                                     ("reader", Book("genre1", "title1", "author1"), TypeError),
                                                     (Reader("name1", 1, "01.01.2001", "1111", []), 1, TypeError),
                                                     (Reader("name1", 1, "01.01.2001", "1111", []), 1.1, TypeError),
                                                     (Reader("name1", 1, "01.01.2001", "1111", []), 'book', TypeError)]
)
def test_return_book_exception(some_library, wrong_reader, wrong_book, expected_exception):
    with pytest.raises(expected_exception):
        some_library.return_book(wrong_reader, wrong_book)


@pytest.mark.parametrize(
    "expected_book, message", [(Book("genre1", "title1", "author1"), 'title1 is added to library')]
)
def test_add_book(some_library, expected_book, message):
    assert message == some_library.add_book(expected_book)


@pytest.mark.parametrize(
    "wrong_book, expected_exception", [(1, TypeError),
                                       (1.1, TypeError),
                                       ("book", TypeError)]
)
def test_add_book_exception(some_library, wrong_book, expected_exception):
    with pytest.raises(expected_exception):
        some_library.add_book(wrong_book)


@pytest.mark.parametrize(
    "expected_book, message", [(Book("genre1", "title1", "author1"), 'title1 is removed from library'),
                               (Book("genre2", "title2", "author2"), 'title2 is not in library')]
)
def test_remove_book(some_library, expected_book, message):
    assert message == some_library.remove_book(expected_book)


@pytest.mark.parametrize(
    "wrong_book, expected_exception", [(1, TypeError),
                                       (1.1, TypeError),
                                       ("book", TypeError)]
)
def test_remove_book_exception(some_library, wrong_book, expected_exception):
    with pytest.raises(expected_exception):
        some_library.remove_book(wrong_book)


@pytest.mark.parametrize(
    "expected_person, message", [(Person("name2", "02.02.2002", "2222"),
                                 'name2 is added to library readers with readers card number 2'),
                                 (Person("name1", "01.01.2001", "1111"),
                                  'name1 is already a library reader')
                                 ]
)
def test_add_reader(some_library, expected_person, message):
    assert message == some_library.add_reader(expected_person)


@pytest.mark.parametrize(
    "wrong_person, expected_exception", [(1, TypeError),
                                         (1.1, TypeError),
                                         ("person", TypeError),
                                         (Reader("name1", 1, "01.01.2001", "1111", []), ValueError)]
)
def test_add_reader_exception(some_library, wrong_person, expected_exception):
    with pytest.raises(expected_exception):
        some_library.add_reader(wrong_person)


@pytest.mark.parametrize(
    "expected_reader, message", [(Reader("name1", 1, "01.01.2001", "1111", []),
                                  'name1 is removed from library readers'),
                                 (Reader("name2", 2, "02.02.2002", "2222", []), 'name2 is not member of library')]
)
def test_remove_reader(some_library, expected_reader, message):
    assert message == some_library.remove_reader(expected_reader)


@pytest.mark.parametrize(
    "wrong_reader, expected_exception", [(1, TypeError),
                                         (1.1, TypeError),
                                         ("person", TypeError),
                                         (Person("name1", "01.01.2001", "1111"), ValueError)]
)
def test_remove_reader_exception(some_library, wrong_reader, expected_exception):
    with pytest.raises(expected_exception):
        some_library.remove_reader(wrong_reader)


def test_status(some_library):
    assert 'name1 has:\nBook title title1, genre genre1, author author1\n' == some_library.status()


@pytest.fixture
def wrong_library_address(some_book, some_reader):
    library_wa = Library(1, "library_phone1", [some_book], [some_reader])
    return library_wa


@pytest.fixture
def wrong_library_phone(some_book, some_reader):
    library_wp = Library('address1', 1, [some_book], [some_reader])
    return library_wp


@pytest.fixture
def wrong_library_books(some_reader):
    library_wb = Library('address1', "library_phone1", 1, [some_reader])
    return library_wb


@pytest.fixture
def wrong_library_readers(some_book):
    library_wr = Library('address1', "library_phone1", [some_book], 1)
    return library_wr


@pytest.fixture
def wrong_empty_lib():
    lib_empty = Library(None, None, None, None)
    return lib_empty


@pytest.mark.parametrize(
    "wrong_lib, expected_exception", [(Library(1, "library_phone1", [some_book], [some_reader]), TypeError),
                                      (Library('address1', 1, [some_book], [some_reader]), TypeError),
                                      (Library('address1', "library_phone1", 1, [some_reader]), TypeError),
                                      (Library('address1', "library_phone1", [some_book], 1), TypeError),
                                      (Library(None, None, None, None), TypeError)]
)
def test_status_exception(wrong_lib, expected_exception):
    with pytest.raises(expected_exception):
        wrong_lib.status()
