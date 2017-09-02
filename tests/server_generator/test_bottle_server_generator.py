import requests

from server_generator.server_generator import MagicRouter
from tests.utils import start_test_bottle_app


class HelloNameURLHandler(MagicRouter):
    route_name = 'hello_name'

    def handler(self):
        return 'hello {}'.format(self.name)


def test_setup():
    route = HelloNameURLHandler()
    start_test_bottle_app(route)
    # url = URL('hello_name')
    # url.get()
    r = requests.get('http://localhost:8080/hello/world')
    assert r.status_code == 200
    assert 'hello world' in r.text
