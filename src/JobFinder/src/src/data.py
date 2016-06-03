import logging
import asyncio
import rethinkdb as db

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def connect():
    db.connect('localhost', 28015).repl()

@asyncio.coroutine
def save(tableName, payload):
    if validate(tableName, payload)

def validate(name, payload):
    pass

if __name__ == "__main__":
    pass
    # connnect()
