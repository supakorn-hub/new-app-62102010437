lass BaseConfig:
    INDEX_TEMPLATE = 'index.html'


class DevConfig(BaseConfig):
    INDEX_TEMPLATE = 'dev.html'

class ProdConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    INDEX_TEMPLATE = 'test.html'


configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}
