import json
from http import HTTPStatus
from app.simple_server.routers.router import Handler
from app.classes.class_Library.class_Library import Library, Book, Person, Reader
from typing import Callable
import psycopg2
from library_config import *

class LibraryResource:
    _library: Library = None

    def __init__(self, library: Library):
        self._library = library

    def _unifunc(self, status_response: int, content_type: str, req: Handler, func):
        req.send_response(status_response)
        req.send_header("content-type", content_type)
        req.end_headers()
        if req.command != "GET":
            length = int(req.headers.get('content-length'))
            body = req.rfile.read(length)
            decoded_body = body.decode()
            data = json.loads(decoded_body)
            if 'readers_card' in data and 'title' in data:
                reader = (Reader(data['full_name'], data['readers_card'], data['date_of_birth'],
                                 data['personal_phone']))
                book = (Book(data['genre'], data['title'], data['author']))
                req.wfile.write(
                    json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                                'method': req.command,
                                'function response': func(reader, book)}).encode()
                )
            if 'title' not in data and 'readers_card' in data:
                reader = (Reader(data['full_name'], data['readers_card'], data['date_of_birth'],
                                 data['personal_phone']))
                req.wfile.write(
                    json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                                'method': req.command,
                                'function response': func(reader)}).encode()
                )
            if 'readers_card' not in data and 'title' not in data:
                person = (Person(data['full_name'], data['date_of_birth'], data['personal_phone']))
                req.wfile.write(
                    json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                                'method': req.command,
                                'function response': func(person)}).encode()
                )
            if 'full_name' not in data:
                book = (Book(data['genre'], data['title'], data['author']))
                req.wfile.write(
                    json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                                'method': req.command,
                                'function response': func(book)}).encode()
                )

        else:
            req.wfile.write(
                json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                            'method': req.command, 'function response': func}).encode()
            )

    def info(self, req: Handler):
        func = self._library.__str__()
        self._unifunc(HTTPStatus.OK, "application/json", req, func)

    def library_books(self, req: Handler):
        func = self._library.library_books.__str__()
        self._unifunc(HTTPStatus.OK, "application/json", req, func)

    def status(self, req: Handler):
        func = self._library.status()
        self._unifunc(HTTPStatus.OK, "application/json", req, func)

    def take_book(self, req: Handler):
        func = self._library.take_book
        self._unifunc(HTTPStatus.OK, "application/json", req, func)

    def return_book(self, req: Handler):
        func = self._library.return_book
        self._unifunc(HTTPStatus.OK, "application/json", req, func)

    def add_book(self, req: Handler):
        func = self._library.add_book
        length = int(req.headers.get('content-length'))
        body = req.rfile.read(length)
        decoded_body = body.decode()
        data = json.loads(decoded_body)
        book = (Book(data['genre'], data['title'], data['author']))
        # func(book)
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            connection.autocommit = True

            #         insert data into table
            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO public."Libraries" (genre, title, author) VALUES
                    ('data['genre']', 'data['title']', 'data['author']');"""
                )
                # connection.commit()
                print("(INFO) Data was successfully inserted")

        except Exception as _ex:
            print("(INFO) Error while working with PosstgreSQL", _ex)
        finally:
            if connection:
                # cursor.close()
                connection.close()
                print("(INFO) PostgreSQL connection closed")
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        req.wfile.write(
            json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response': 'book added'}).encode())

    def remove_book(self, req: Handler):
        func = self._library.remove_book
        self._unifunc(HTTPStatus.OK, "application/json", req, func)

    def add_reader(self, req: Handler):
        func = self._library.add_reader
        self._unifunc(HTTPStatus.OK, "application/json", req, func)

    def remove_reader(self, req: Handler):
        func = self._library.remove_reader
        self._unifunc(HTTPStatus.OK, "application/json", req, func)






