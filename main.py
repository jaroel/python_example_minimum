from wsgiref.simple_server import make_server

import dehulde
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response("Hello %(name)s!" % request.matchdict)


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("hello", "/hello/{name}")
        config.add_view(hello_world, route_name="hello")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 8080, app)
    print("Here we go!")
    print("Try this by running 'curl http://localhost:8080/hello/world'")
    server.serve_forever()
