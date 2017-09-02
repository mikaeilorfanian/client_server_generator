from threading import Thread
import os

from configurator.server_conf import parse_server_conf
from server_generator.server_generator import BottleServer
from settings import Settings, FILE_CONFIG_TYPE


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_SETTING_FILE_PATH = os.path.join(BASE_PATH, 'test_server_client_conf.yaml')


test_settings = {
    'type': FILE_CONFIG_TYPE,
    'path': TEST_SETTING_FILE_PATH,
}


test_server_conf = parse_server_conf(Settings(test_settings))



def bottle_app_runner(route):
    app = BottleServer(
        routes=[route], server_conf=test_server_conf
    )
    app.run()


def start_test_bottle_app(route):
    p = Thread(target=bottle_app_runner, args=(route,), daemon=True)
    p.start()
    import time; time.sleep(1) # wait for bottle server to start
