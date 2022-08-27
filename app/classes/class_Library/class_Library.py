class Book:
    genre: str = None
    title: str = None
    author: str = None

    def __init__(self, genre: str, title: str, author: str):
        self.genre = genre
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.genre == other.genre and self.title == other.title and self.author == other.author

    def __str__(self):
        return f'Book title {self.title}, genre {self.genre}, author {self.author}\n'

    def __repr__(self):
        return f'{self.title}, {self.genre}, {self.author}'


'''
 class LibraryBook(Book):
     copies: int = 0
     
     def add_copy(self):
         self.copies += 1
     def remove_copy(self):
         self.copies -= 1
     def copies_number(self):
         self.copies = 
'''


class Person:
    full_name: str = None
    date_of_birth: str = None
    personal_phone: str = None

    def __init__(self, full_name: str, date_of_birth: str, personal_phone: str):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.personal_phone = personal_phone

    def __eq__(self, other):
        return self.full_name == other.full_name and self.date_of_birth == other.date_of_birth \
               and self.personal_phone == other.personal_phone

    def __str__(self):
        return f'Full name {self.full_name}, date of birth {self.date_of_birth}\n'


class Reader(Person):
    readers_card: int = None
    readers_books: list[Book] = []

    def __init__(self, full_name: str, readers_card: int, date_of_birth: str, personal_phone: str):
        super().__init__(full_name, date_of_birth, personal_phone)
        self.readers_card = readers_card
        self.readers_books = []

    def __str__(self):
        return f'Full name {self.full_name}, readers card {self.readers_card}, date of birth {self.date_of_birth},' \
               f' phone number {self.personal_phone}, books {self.readers_books}\n'

    def __repr__(self):
        return f'{self.full_name}, {self.readers_card}, {self.date_of_birth}, {self.personal_phone}, ' \
               f'{self.readers_books}'

    def __eq__(self, other):
        return self.full_name == other.full_name and self.date_of_birth == other.date_of_birth and self.personal_phone == other.personal_phone and self.readers_card == other.readers_card and self.readers_books == other.readers_books


class Library:
    address: str = None
    library_phone: str = None
    library_books: list[Book] = []
    readers: list[Reader] = []
    readers_number = 0

    def __init__(self, address: str, library_phone: str, library_books: list[Book], readers: list[Reader]):
        self.address = address
        self.library_phone = library_phone
        self.library_books = library_books
        self.readers = readers
        self.readers_number = len(self.readers)

    def __str__(self):
        return f'Library address: {self.address}, library phone: {self.library_phone}' \
               f'\nbooks:\n{", ".join([str(x) for x in self.library_books])}\n' \
               f'\nreaders:\n{"".join([str(r) for r in self.readers])}\n'

    def take_book(self, reader: Reader, book: Book):
        if not isinstance(reader, Reader):
            raise TypeError(f'Argument "reader" must be a Reader class, not {type(reader)}')
        if not isinstance(book, Book):
            raise TypeError(f'Argument "book" must be a Book class, not {type(book)}')
        if reader not in self.readers:
            return f'{reader.full_name} is not member of library'
        else:
            if book in self.library_books:
                self.library_books.remove(book)
                reader.readers_books.append(book)
                return f'{reader.full_name} took {book.title}'
            else:
                return f'{book.title} unavailable'

    def return_book(self, reader: Reader, book: Book):
        if not isinstance(reader, Reader):
            raise TypeError(f'Argument "reader" must be a Reader class, not {type(reader)}')
        if not isinstance(book, Book):
            raise TypeError(f'Argument "book" must be a Book class, not {type(book)}')
        if reader not in self.readers:
            return f'{reader.full_name} is not member of library'
        else:
            if book in reader.readers_books:
                reader.readers_books.remove(book)
                self.library_books.append(book)
                return f'{reader.full_name} returned {book.title}'
            else:
                return f'{book.title} unavailable'

    def status(self):
        if not isinstance(self.address, str):
            raise TypeError(f'{self.address} should be string, not {type(self.address)}')
        if not isinstance(self.library_phone, str):
            raise TypeError(f'{self.library_phone} should be string, not {type(self.library_phone)}')
        if not isinstance(self.readers, list):
            raise TypeError(f'{self.readers} should be list of Reader, not {type(self.readers)}')
        if not isinstance(self.library_books, list):
            raise TypeError(f'{self.library_books} should be list of Book, not {type(self.library_books)}')
        if self.address is None or self.library_phone is None or self.library_books is None or self.readers is None:
            raise ValueError(f'All parameters of library should be defined')
        list_readers_books = []
        for reader in self.readers:
            if reader in self.readers:
                list_readers_books.append(f'{reader.full_name} has:\n{"".join([str(x) for x in reader.readers_books])}')
        return ''.join(map(str, list_readers_books))

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError(f'Argument "book" must be a Book class, not {type(book)}')
        self.library_books.append(book)
        return f'{book.title} is added to library'

    def remove_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError(f'Argument "book" must be a Book class, not {type(book)}')
        if book in self.library_books:
            self.library_books.remove(book)
            return f'{book.title} is removed from library'
        else:
            return f'{book.title} is not in library'

    def add_reader(self, person: Person):
        if isinstance(person, Reader):
            raise ValueError(f'Existing reader cant be re-registered')
        if not isinstance(person, Person):
            raise TypeError(f'Argument "person" must be a Person class, not {type(person)}')
        if person in self.readers:
            return f'{person.full_name} is already a library reader'
        if self.readers == []:
            readers_card = 1
        else:
            readers_card = self.readers[-1].readers_card + 1
        readers_books = []
        person = Reader(person.full_name, readers_card, person.date_of_birth, person.personal_phone)
        self.readers.append(person)
        self.readers_number += 1
        return f'{person.full_name} is added to library readers with readers card number {person.readers_card}'

    def remove_reader(self, reader: Reader):
        if isinstance(reader, Person):
            raise ValueError(f'Unregistered person cant be removed from library readers')
        if not isinstance(reader, Reader):
            raise TypeError(f'Argument "reader" must be a Reader class, not {type(reader)}')
        if reader in self.readers:
            self.readers.remove(reader)
            self.readers_number -= 1
            return f'{reader.full_name} is removed from library readers'
        else:
            return f'{reader.full_name} is not member of library'


book1 = Book('comedy', 'Book Title 1', 'Author1')
book2 = Book('drama', 'Book Title 2', 'Author2')
book3 = Book('fantasy', 'Book Title 3', 'Author3')

reader1 = Reader("Name1", 1, "01.01.2001", "1111")
reader2 = Reader("Name2", 2, "02.02.2002", "2222")
reader3 = Reader("Name3", 3, "03.03.2003", "3333")

my_library = Library('', '', [], [])

if __name__ == "__main__":
    book1 = Book('comedy', 'Book Title 1', 'Author1')
    book2 = Book('drama', 'Book Title 2', 'Author2')
    book3 = Book('fantasy', 'Book Title 3', 'Author3')

    reader1 = Reader("Name1", 1, "01.01.2001", "1111")
    reader2 = Reader("Name2", 2, "02.02.2002", "2222")
    reader3 = Reader("Name3", 3, "03.03.2003", "3333")

    library1 = Library('a1b1', '094', [book1, book2, book3], [reader1, reader2, reader3])
    # print(book1, book2, book3)
    # print(reader1, reader2, reader3)
    # print(library1)
    # print(library1.library_books)
    # wtr = Book('comedy', 'Book Title 1', 'Author1')
    # print(wtr in library1.library_books)
    # print(library1.take_book(reader1, book1))
    # print(library1.take_book(reader1, book2))
    # print(library1.take_book(reader2, book3))
    # print(library1.status())
    # print(library1)
    # reader4 = Person("Name4", "04.04.2004", "4444")
    # print(library1.add_reader(reader4))
    # print(library1.readers_number)
    # print(library1.readers[3])
    person1 = Person('person_name', '05.05.2005', '5555')
    print(library1.add_reader(Person('person_name', '05.05.2005', '5555')))
    # library1.take_book(library1.readers[3], book1)
    print(library1.take_book(Reader("person_name", 4, '05.05.2005', '5555'), Book('drama', 'Book Title 2', 'Author2')))
    # print(library1.return_book(library1.readers[3], book2))
    # print(Reader("person_name", 4, '05.05.2005', '5555') is library1.readers[3])
    # print(Book('fantasy', 'Book Title 3', 'Author3') is library1.library_books[0])
    # print(Book('fantasy', 'Book Title 3', 'Author3') is book3)
    # print(book3 is library1.library_books[0])
    # print(Book('fantasy', 'Book Title 3', 'Author3') in library1.library_books)
    print(library1)

