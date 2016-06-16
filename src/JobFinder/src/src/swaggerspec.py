import os
from flask import Flask, jsonify, request, session, g, redirect, url_for, abort, \
    render_template, flash
from flask_swagger import swagger

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Nurse"

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

@app.route('/Job', methods=['Get'])
def Job():
    pass

def Apartment():
    pass

app.config.from_envvar('Swagger_Settings', silent=True)
