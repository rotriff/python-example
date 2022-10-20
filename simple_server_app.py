from app.simple_server.routers.router import Router, Handler
from app.simple_server.routers.routes import get_routes
from app.simple_server.library_resource import LibraryResource
from app.classes.class_Library.class_Library import Library, my_library
from app.simple_server.simple_server import run_server
from http.server import HTTPServer

if __name__ == "__main__":
    library = my_library
    library_resource = LibraryResource(library)
    routes = get_routes(library_resource)
    router = Router()

    for route in routes:
        router.add(route["method"], route["path"], route["call"])

    Handler.ROUTER = router
    run_server(HTTPServer, Handler)
