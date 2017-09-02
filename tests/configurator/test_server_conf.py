from configurator.server_conf import Route
from tests.utils import server_conf_for_tests


class TestRouteClass:

    def test_correct_raw_config_parsed_correctly(self):
        raw_conf = server_conf_for_tests.get_raw_route_conf('hello_name')
        r = Route(raw_conf)

        assert r.name == raw_conf['route_name']
        assert r.route == raw_conf['route']
        assert len(r.route_variables) == 1
        assert 'name' in r.route_variables

    def test_more_than_one_variable_extracted_correctly(self):
        raw_conf = server_conf_for_tests.get_raw_route_conf('hello_name2')
        r = Route(raw_conf)

        assert len(r.route_variables) == 2
        assert 'first_name' in r.route_variables
        assert 'last_name' in r.route_variables
