import os
import logging
import sqlalchemy
from threading import Lock
from sqlalchemy.orm import sessionmaker, scoped_session


class Singleton(type):
    """ This is a Singleton metaclass. All classes affected by this metaclass 
    have the property that only one instance is created for each set of arguments 
    passed to the class constructor."""

    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(cls, bases, dict)
        cls._instanceDict = {}

    def __call__(cls, uri=None, _reset=False):
        if not uri:
            uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
        if not uri:
            raise ValueError(f'Invalid database uri: {uri}.')
        argset = frozenset([uri])
        if argset not in cls._instanceDict or _reset:
            cls._instanceDict[argset] = super(Singleton, cls).__call__(uri=uri)
        return cls._instanceDict[argset]

class Database(metaclass=Singleton):
    def __init__(self, uri=None):
        try:
            logger = logging.getLogger(__name__)

            pool_recycle = os.environ.get(
                'SQLALCHEMY_POOL_RECYCLE', 3600)

            pool_pre_ping = os.environ.get(
                'POOL_PRE_PING', False)
            
            logger.info('Initializing connection with database...')
           
            self.engine = sqlalchemy.create_engine(
                uri, 
                pool_recycle=pool_recycle, 
                pool_pre_ping=pool_pre_ping
            )
            self.Session = scoped_session(sessionmaker(bind=self.engine))
            logger.info('Database connection established succeed to {}\n'.format(uri))
        except Exception as e:
            logger.exception("Unexpected error! Could not connect to database")
            raise e

    @staticmethod
    def to_dict(result_proxy):
        return [dict(r.items()) for r in result_proxy]