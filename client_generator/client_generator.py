from configurator.server_conf import server_config, ServerConfig


class URL:

    def __init__(self, server_conf: ServerConfig, route_name: str):
        self.server_config = server_conf
        self.route_name = route_name

    def get_full_url(self, **kwargs):
        path = self.server_config.self.route_name.replace('<', '{').replace('>', '}').format(kwargs)
        return server_config.domain + path


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
