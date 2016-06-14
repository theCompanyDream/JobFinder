"""
ToDo:  I want to add validation to these objects and log the outcome
"""

# from wtforms import Form, BooleanField, StringField, validators

class Job(Form):
    database_name = "JobDb"
    table_name = "Jobs"
    order_by = "date"

class Apartment:
    pass

class Events:
    pass
