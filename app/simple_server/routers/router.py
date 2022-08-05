from app.classes.class_Library.class_Library import my_library

routes = {
    "library/books": {
        "call": ''.join(map(str, my_library.library_books))
    }
}

'''
routes = [
    {
        'method': 'GET',
        'path': 'v1/library/books',
        'call': my_library.library_books()
    },
    {
        'method': 'POST',
        'path': 'v1/library/books',
        'call': my_library.add_book()
    },
    {
        'method': 'DELETE',
        'path': 'v1/library/books',
        'call': my_library.remove_book()
    }
]
'''
