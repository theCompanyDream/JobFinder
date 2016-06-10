import rethinkdb as db

db.connect('192.168.99.100', 28015).repl()
db.db_create('Jobdb').table_create("JobListing").run()
