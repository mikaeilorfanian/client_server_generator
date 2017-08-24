import requests

from configurator.server_conf import server_config


class URL:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_full_path(self, **kwargs):
        self.address.replace('<', '{').replace('>', '}').format(kwargs)


class GenerateURLs:

    def __init__(self):
        pass

    def generate_urls(self):
        for route in server_config.routes:
            setattr(
                self,
                route.name,
                URL(route)
            )
