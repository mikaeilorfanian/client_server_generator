import os

from configurator.server_conf import parse_server_conf
from settings import Settings, FILE_CONFIG_TYPE


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_SETTING_FILE_PATH = os.path.join(BASE_PATH, 'test_server_client_conf.yaml')


test_settings = {
    'type': FILE_CONFIG_TYPE,
    'path': TEST_SETTING_FILE_PATH,
}


test_server_conf = parse_server_conf(Settings(test_settings))
