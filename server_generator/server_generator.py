from .server_conf import server_config


class BaseServerGenerator:

    pass


class BottleServer(BaseServerGenerator):

    def __init__(self, *routes):
        self.config = server_config
        self.routes = routes

    def run(self, host='localhost', port=8080):
        self._make_routes()
        from bottle import run
        run(host=host, port=port, debug=True)

    def _make_routes(self):
        for route in self.routes:
            route._generate_route()


class MagicRouter:

    def __init__(self):
        pass

    def _generate_route(self):
        from bottle import route

        @route(server_config(self.route_name).route)
        def generic_handler(name):
            self.set_route_variable(name)
            return self.handler()

    def set_route_variable(self, route_variable_value):
        setattr(
            self,
            server_config(self.route_name).route_variable,
            route_variable_value
        )
