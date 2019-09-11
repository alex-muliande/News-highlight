
import os
class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    BASE_URL= 'https://newsapi.org/v2/sources?language=en&apiKey='
    ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey='


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
