from app.simple_server.library_resource import LibraryResource
from typing import Callable
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler


def get_routes(library_resource: LibraryResource):
    routes = [
        {
            'method': 'GET',
            'path': '/library/books',
            'call': library_resource.library_books
        },
        {
            'method': 'GET',
            'path': '/library',
            'call': library_resource.status
        },
        {
            'method': 'POST',
            'path': '/library/books/add',
            'call': library_resource.add_book
        },
        {
            'method': 'POST',
            'path': '/library/books/take',
            'call': library_resource.take_book
        },
        {
            'method': 'POST',
            'path': '/library/books/return',
            'call': library_resource.return_book
        },
        {
            'method': 'DELETE',
            'path': '/library/books/delete',
            'call': library_resource.remove_book
        },
        {
            'method': 'POST',
            'path': '/library/readers/add',
            'call': library_resource.add_reader
        },
        {
            'method': 'DELETE',
            'path': '/library/readers/delete',
            'call': library_resource.remove_reader
        }
    ]
    return routes

'''
from app.classes.class_Library.class_Library import my_library, Library

routes = {
    "GET": {
        "/library": {
            "call": my_library.__str__
        },
        '/': {
            "call": "my_project"
        }
    },
    "POST": {
        "/library/books": {
            "call": my_library.add_book
        }
    },
    "DELETE": {
        "/library/book": {
            "call": my_library.remove_book
        }
    }

}
'''