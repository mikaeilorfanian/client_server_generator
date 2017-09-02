from configurator.server_conf import server_config, ServerConfig


class URL:

    def __init__(self, route_name: str, server_conf: ServerConfig=server_config):
        self.server_config = server_conf
        self.route_name = route_name

    def get_full_url(self, **kwargs):
        path = self.server_config(self.route_name).route.replace('<', '{').replace('>', '}').format(**kwargs)
        if path[0] == '/':
            path = path[1:]
        if server_config.domain[-1] == '/':
            domain = server_config[:-1]
        else:
            domain = server_config.domain

        return domain + '/' + path


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
