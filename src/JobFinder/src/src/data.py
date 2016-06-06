import configparser
import logging
import asyncio
import rethinkdb as db

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def connect():
    db.connect('192.168.99.100', 32770).repl()

@asyncio.coroutine
def save(tableName, payload):
    logger.debug("Processing Table {0}\n\t with payload:\n {1}".format(tableName, payload))
    if validate(tableName, payload):
        pass
    performSave(tableName, payload)

def validate(name, payload):
    pass

def performSave(name, payload):
    connect()
    db.table('users').insert(payload)

if __name__ == "__main__":
    logger.debug("hello")
    config = configparser.ConfigParser()
    config.read('setup.cfg')
    print(config.sections())
    # connnect()
