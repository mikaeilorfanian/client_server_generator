from configurator.server_conf import server_config


class BaseServerGenerator:

    def __init__(self, routes, server_conf):
        self.config = server_conf
        self.routes = routes


class BottleServer(BaseServerGenerator):

    def __init__(self, routes, server_conf=server_config):
        super().__init__(routes, server_conf)

    def run(self, host='localhost', port=8080):
        from bottle import run

        self._make_routes()

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
            server_config(self.route_name).route_variables[0],
            route_variable_value
        )
