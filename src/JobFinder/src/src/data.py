import configparser
import logging
import rethinkdb as db

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def connect():
    db.connect('192.168.99.100', 28015).repl()

def save(tableName, payload):
    print("Processing Table {0}\n\t with payload:\n {1}".format(tableName, payload))
    if validate(tableName, payload):
        pass
    performSave(tableName, payload)

def validate(name, payload):
    pass

def performSave(name, payload):
    connect()
    product = object
    ifexists = db.table(name).get(payload).run()

    if ifexists :
        product = db.table(name).update(ifexists).run()
    else:
        product = db.table(name).insert(payload).run()

    return product

if __name__ == "__main__":
    save('JobTable', {'Jobs': "Tim jobs yay"})
