import json
from http import HTTPStatus
from app.simple_server.routers.router import Handler
from app.classes.class_Library.class_Library import Library, Book, Person, Reader


class LibraryResource:
    _library: Library = None

    def __init__(self, library: Library):
        self._library = library

    def library_books(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        func = self._library.library_books.__str__()
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response':  func}).encode()
        )

    def status(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        func = self._library.status()
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response': func}).encode()
        )

    def take_book(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        length = int(req.headers.get('content-length'))
        body = req.rfile.read(length)
        decoded_body = body.decode()
        data = json.loads(decoded_body)
        func = self._library.take_book(Reader(data['full_name'], data['readers_card'], data['date_of_birth'],
                                              data['personal_phone'], data['readers_books']),
                                       Book(data['genre'], data['title'], data['author']))
        req.wfile.write(
            json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response':  func}).encode()
        )

    def return_book(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        length = int(req.headers.get('content-length'))
        body = req.rfile.read(length)
        decoded_body = body.decode()
        data = json.loads(decoded_body)
        func = self._library.return_book(Reader(data['full_name'], data['readers_card'], data['date_of_birth'],
                                                data['personal_phone'], data['readers_books']),
                                         Book(data['genre'], data['title'], data['author']))
        req.wfile.write(
            json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response':  func}).encode()
        )

    def add_book(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        length = int(req.headers.get('content-length'))
        body = req.rfile.read(length)
        decoded_body = body.decode()
        data = json.loads(decoded_body)
        func = self._library.add_book(Book(data['genre'], data['title'], data['author']))
        req.wfile.write(
            json.dumps({'server_name': 'Library HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response':  func}).encode()
            # TODO response functions instead of above lines 1:35:00
        )

    def remove_book(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        length = int(req.headers.get('content-length'))
        body = req.rfile.read(length)
        decoded_body = body.decode()
        data = json.loads(decoded_body)
        func = self._library.remove_book(Book(data['genre'], data['title'], data['author']))
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response':  func}).encode()
        )

    def add_reader(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        length = int(req.headers.get('content-length'))
        body = req.rfile.read(length)
        decoded_body = body.decode()
        data = json.loads(decoded_body)
        func = self._library.add_reader(Person(data['full_name'], data['date_of_birth'],
                                               data['personal_phone']))
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response':  func}).encode()
        )

    def remove_reader(self, req: Handler):
        req.send_response(HTTPStatus.OK)
        req.send_header("content-type", "application/json")
        req.end_headers()
        length = int(req.headers.get('content-length'))
        body = req.rfile.read(length)
        decoded_body = body.decode()
        data = json.loads(decoded_body)
        func = self._library.remove_reader(Reader(data['full_name'], data['readers_card'], data['date_of_birth'],
                                                  data['personal_phone'], data['readers_books']))
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Vova Taran', 'path': req.path,
                        'method': req.command,
                        'function response':  func}).encode()
        )

