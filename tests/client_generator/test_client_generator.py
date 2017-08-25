from client_generator.client_generator import URL
from tests.utils import test_server_conf


class TestURLGetFullPathMethod:

    def test_correct_url_returned_when_theres_one_url_variable(self):
        url = URL(test_server_conf, 'hello_name')
        assert url.get_full_url(name='G') == 'localhost/hello/G'
