import os
from distutils.util import strtobool
from pathlib import Path


class Config():
    APP_ROOTDIR = os.path.abspath(os.path.dirname(__file__))
    RESTFUL_JSON = {'ensure_ascii': False}
    SQLALCHEMY_POOL_RECYCLE = os.getenv('SQLALCHEMY_POOL_RECYCLE', 3600)
    POOL_PRE_PING = bool(strtobool(os.getenv('POOL_PRE_PING', 'False')))
    DEBUG = bool(os.getenv('DEBUG', False))
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', None)
    LOCALE = os.getenv('LOCALE', 'jp')

    DEFAULT_ERROR_PREFIX = 'errors'
    DATA_PATH = str(Path(__file__).parent.parent / 'data')
