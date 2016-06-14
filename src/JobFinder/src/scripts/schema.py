"""
This creates the default tables for rethinkdb may possibly be moved to a dockerfile but for now it's fine here
"""
import rethinkdb as r

jobDb = 'JobDb'

conn = r.connect('192.168.99.100', 32769).repl()
r.db_create(jobDb).run()

for table in ["Jobs", 'Apartments', 'Events']:
    r.db(jobDb).table_create(table).run()
