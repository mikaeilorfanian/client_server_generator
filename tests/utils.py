from configurator.server_conf import parse_server_conf
import settings


test_settings = {
    'type': settings.FILE_CONFIG_TYPE,
    'path': '/tests/test_server_client_conf.yaml',
}


test_server_conf = parse_server_conf(test_settings)
