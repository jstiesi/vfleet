#! /usr/bin/python3

"""
This is an example Flask | Python | Psycopg2 | PostgreSQL
application that connects to the 7dbs database from Chapter 2 of
_Seven Databases in Seven Weeks Second Edition_
by Luc Perkins with Eric Redmond and Jim R. Wilson.
The CSC 315 Virtual Machine is assumed.

John DeGood
degoodj@tcnj.edu
The College of New Jersey
Spring 2020

----

One-Time Installation

You must perform this one-time installation in the CSC 315 VM:

# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask

----

Usage

To run the Flask application, simply execute:

export FLASK_APP=app.py 
flask run
# then browse to http://127.0.0.1:5000/

----

References

Flask documentation:  
https://flask.palletsprojects.com/  

Psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
"""

import psycopg2
import re
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows
 
# app.py
app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
    # provide names of columns from cost table for dropdown in economic form
    colnames = connect('select column_name from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME=\'cost\';')
    # remove the first "vin" attribute, do not want in dropdown
    del colnames[0]

    return render_template('my-form.html', colnames=colnames)

# handle economic fields POST and serve result web page
@app.route('/economic-handler', methods=['POST'])
def economic_handler():
    # user's selected attribute from dropdown menu
    attr = request.form['attr']

    # user's input cost value
    cost = request.form['cost']

    # radio button choice (asc/desc)
    sort = request.form['sort']

    # database query
    rows = connect('SELECT ' + attr + ', VEHICLE.VIN, Name, Vehi_type, Fuel_type, Mileage_yr FROM VEHICLE INNER JOIN COST ON VEHICLE.VIN=COST.VIN WHERE ' + attr + ' < ' + cost + ' ORDER BY ' + attr + ' ' + sort + ';')

    # to show type of results being displayed
    form = "Economic"
    # label columns of results table
    heads = [attr, 'vin','name','vehi_type','fuel_type','mileage_yr']

    return render_template('my-result.html', rows=rows, heads=heads, form=form)

# handle environmental fields POST and serve result web page
@app.route('/environmental-handler', methods=['POST'])
def environmental_handler():
    # user's input amount value
    cost = request.form['amount']

    # radio button choice (asc/desc)
    sort = request.form['sort']

    rows = connect('SELECT Amount, POLLUTANT.Name, VIN, VEHICLE.Name, Vehi_type, Fuel_type, Mileage_yr FROM VEHICLE INNER JOIN POLLUTANT ON VEHICLE.VIN=POLLUTANT.PVIN WHERE Amount < ' + cost + ' ORDER BY Amount ' + sort + ';')
    
    # to show type of results being displayed
    form = "Environmental"
    # label columns of results table
    heads = ['amount', 'pollutant.name', 'vin', 'vehicle.name', 'vehi_type','fuel_type','mileage_yr']
    
    return render_template('my-result.html', rows=rows, heads=heads, form=form)

if __name__ == '__main__':
    app.run(debug = True)
