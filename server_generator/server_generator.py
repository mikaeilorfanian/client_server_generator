from .server_conf import server_config


class BaseServerGenerator:

    def


class BottleServerGenerator(BaseServerGenerator):

    def __init__(self):
        self.config = server_config

    def run(self, host, port):
        from bottle import run
        run(host=host, port=port)

    def __call__(self, decorator_argument_called_route_name):
        from bottle import route
        def wrap(f):
            @route(server_config(route_name).route)
            
            def wrapped_f():
                pass
            return wrapped_f
        return wrap

