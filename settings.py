FILE_CONFIG_TYPE = 'file'
REMOTE_RAW_PAGE = 'remote_raw_page'


CONFIG = {
    'type': REMOTE_RAW_PAGE,
    'path': 'https://raw.githubusercontent.com/mikaeilorfanian/client_server_generator/master/server_client_conf.yaml',
}


class Settings:

    def __init__(self, config):
        self.config = config

    def __getattr__(self, item):
        return self.config[item]


config_settings = Settings(CONFIG)
