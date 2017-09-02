import pytest

from client_generator.client_generator import URL
from tests.utils import server_conf_for_tests


class TestURLGetFullPathMethod:

    def test_correct_url_returned_when_theres_one_url_variable(self):
        url = URL(server_conf_for_tests, 'hello_name')
        assert url.get_full_url(name='G') == 'localhost/hello/G'

    def test_correct_url_returned_when_there_are_two_url_variables(self):
        url = URL(server_conf_for_tests, 'hello_name2')
        assert url.get_full_url(first_name='Benjamin', last_name='Nate') == 'localhost/hello2/Benjamin/Nate'

    def test_route_variable_missing(self):
        url = URL(server_conf_for_tests, 'hello_name')

        with pytest.raises(KeyError):
            url.get_full_url() == 'localhost/hello/G'

    def test_route_variables_are_given_out_of_order(self):
        url = URL(server_conf_for_tests, 'hello_name2')
        assert url.get_full_url(last_name='Nate', first_name='Benjamin') == 'localhost/hello2/Benjamin/Nate'

    def test_route_without_any_variables(self):
        url = URL(server_conf_for_tests, 'hello_world')
        assert url.get_full_url() == 'localhost/hello/world'
