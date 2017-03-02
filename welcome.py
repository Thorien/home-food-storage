import os
from flask import Flask, jsonify, render_template
import sqlite3 as lite
import sys

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/validatedb')
def db_info():
    con = None

    try:
        con = lite.connect('test.db')
        db_handle = con.cursor()
        db_handle.execute('SELECT SQLITE_VERSION()')
        data = db_handle.fetchone()
        print("SQLite version: {1}".format(data))
    except lite.Error as err:
        print
        "Error %s:" % err[0]
        sys.exit(1)
    finally:
        if con:
            con.close()

"""
@app.route('/myapp')
def welcome_to_my_app():
    return 'Welcome again to my app running on Bluemix!'


@app.route('/api/people')
def get_people():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

"""


@app.route('/say/<name>')
def say_hello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results = message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='localhost', port=int(port))
