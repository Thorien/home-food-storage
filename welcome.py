import os
from flask import Flask, jsonify, render_template
import sqlite3 as lite
import sys
import pdb
import shoppinglist_class
from db_manip_class import DBManip

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/testdb')
def db_info():
    con = None

    try:
        con = lite.connect('hfs.db')
        db_manip = DBManip(con.cursor())
        x = db_manip.execute_query('SELECT SQLITE_VERSION()')
        tpl_db_version = "SQLite version: {d}".format(d=x)
    except lite.Error as err:
        tpl_db_version = "Error %s:" % err
        sys.exit(1)
    finally:
        if con:
            con.close()
            pass
    return render_template('db_info.html', message=tpl_db_version)


@app.route('/createdb')
def db_create():
    con = None

    try:
        pdb.set_trace()
        con = lite.connect('hfs.db')
        db_manip = DBManip(con.cursor())
        if db_manip.create_tables():
            status = "DB tables created."
        else:
            status = "Something went wrong."
    except lite.Error as err:
        status = "Error %s:" % err
        sys.exit(1)
    finally:
        if con:
            con.close()
            pass
    return render_template('db_info.html', message=status)


@app.route('/say/<name>')
def say_hello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results = message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='localhost', port=int(port))
