import configparser
import logging
import rethinkdb as r

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def connect():
    r.connect('192.168.99.100', 32769).repl()

def save(tableName, payload):
    # print("Processing Table {0}\n\t with payload:\n {1}".format(tableName, payload))
    if validate(tableName, payload):
        pass
    for x in payload['results']:
        performSave(tableName, payload['results'])

def validate(name, payload):
    pass

def performSave(name, payload):
    connect()
    product = object
    cursor = r.db("Job").table(name).filter(payload).run()
    toList = [table for table in cursor]


    if len(toList) > 0:
        product = r.db("Job").table(name).update(payload).run()
    else:
        product = r.db("Job").table(name).insert(payload).run()

    print("Performed Insert: {0} {1} ".format(cursor, product))

    return product

if __name__ == "__main__":
    save('JobTable', {'Jobs': "Tim jobs yay"})
