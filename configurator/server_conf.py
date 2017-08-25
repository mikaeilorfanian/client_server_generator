from typing import List
import yaml

import requests

import settings


def read_config_file(file_name):
    with open(file_name, 'r') as stream:
        conf = yaml.load(stream)
    return conf


def read_config_from_remoate_raw_page(page_url):
    r = requests.get(page_url)
    return yaml.load(r.text)


def parse_server_conf(settings):

    if settings.CONFIG['type'] == settings.FILE_CONFIG_TYPE:
        conf = read_config_file(settings.CONFIG['path'])
    elif settings.CONFIG['type'] == settings.REMOTE_RAW_PAGE:
        conf = read_config_from_remoate_raw_page(settings.CONFIG['path'])
    else:
        raise ValueError('Wrong configuration set in settings.py!')

    return ServerConfig(conf)


class Route:

    def __init__(self, raw_config):
        self.name = raw_config['route_name']
        self.route = raw_config['route']
        self.http_method = raw_config['http_method']
        self.route_variable = raw_config['route_variable']


class ServerConfig:

    def __init__(self, conf: dict):
        self.raw_config = conf
        self.raw_routes_conf = conf['server']['routes']

    def __call__(self, route_name: str) -> Route:
        for route in self.routes:
            if route.name == route_name:
                return route
        raise ValueError('Route name not found')

    @property
    def routes(self) -> List[Route]:
        return [Route(raw_route_conf) for raw_route_conf in self.raw_routes_conf]

    def backend(self) -> str:
        return self.raw_config['server']['server_backend']

    @property
    def domain(self) -> str:
        return self.raw_config['server']['domain']


server_config = parse_server_conf(settings)
