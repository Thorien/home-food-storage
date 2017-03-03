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
        tpl_db_version = "SQLite version: {1}".format(str(data))
    except lite.Error as err:
        tpl_db_version = "Error %s:" % err
        sys.exit(1)
    finally:
        if con:
            con.close()
    return render_template('db_info.html', name=tpl_db_version)


@app.route('/say/<name>')
def say_hello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results = message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='localhost', port=int(port))
