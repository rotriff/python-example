from app.classes.class_Library.class_Library import my_library

routes = {
    "GET": {
        "/library": {
            "call": str(my_library)
        },
        '/': {
            "call": "my_project"
        }
    },
    "POST": {
        "/library/book": {
            "call": my_library.add_book()
        }
    },
    "DELETE": {
        "/library/book": {
            "call": my_library.remove_book()
        }
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
