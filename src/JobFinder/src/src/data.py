import configparser
import logging
import rethinkdb as r

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def connect():
    r.set_loop_type("asyncio")
    r.connect('192.168.99.100', 32769).repl()

def save(tableName, *payload):
    # logging.debug("Processing Table {0}\n\t with payload:\n {1}".format(tableName, payload))
    for table in payload:
        if validate(tableName, table):
            pass
        perform_save(tableName, table)

def validate(name, *payload):
    pass

def perform_save(name, payload):
    connect()
    product = object
    cursor = r.db("JobDb").table(name).filter(payload).run()
    toList = [table for table in cursor]

    if len(toList) > 0:
        product = r.db("JobDb").table(name).update(payload).run()
    else:
        product = r.db("JobDb").table(name).insert(payload).run()

    logging.debug("Performed Insert: {0} {1} ".format(cursor, product))

    return product

def GetUniqueLocations():
    connect()
    cursor = r.db('JobDb').table('Job').pluck('formattedLocation').distinct().run()
    return [x for x in cursor]

async def Get(conn, name, pageNumber = 1, pageSize = 10):
    connect()
    return r.db("JobDb").table(name).slice(pageNumber, pageSize)

async def InsertOrUpdate():
    logging.debug('')
    pass

async def Delete():
    pass

async def Distinct():
    pass

if __name__ == "__main__":
    parser = configparser.ConfigParser()
    found = parser.read("setup.cfg")
    for section in found:
        logging.debug(section)
    # save('JobTable', {'Jobs': "Tim jobs yay"})
