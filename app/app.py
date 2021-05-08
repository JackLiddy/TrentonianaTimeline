#! /usr/bin/python3

"""
ONE-TIME SETUP

To run this example in the CSC 315 VM you first need to make
the following one-time configuration changes:

# set the postgreSQL password for user 'lion'
sudo -u postgres psql
    ALTER USER lion PASSWORD 'lion';
    \q

# install pip for Python 3
sudo apt update
sudo apt install python3-pip

# install psycopg2
pip3 install psycopg2-binary

# install flask
pip3 install flask

# logout, then login again to inherit new shell environment
"""

"""
CSC 315
Spring 2021
John DeGood

# usage
export FLASK_APP=app.py 
flask run

# then browse to http://127.0.0.1:5000/

Purpose:
Demonstrate Flask/Python to PostgreSQL using the psycopg adapter.
Connects to the 7dbs database from "Seven Databases in Seven Days"
in the CSC 315 VM.

For psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
"""



import psycopg2
from config import config
from flask import Flask, render_template, request, flash, redirect, request, session, abort
import os

def connect(query):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters from database.ini
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

 
    
 
# serve homepage at root dir
@app.route("/")   
def homepage():
    return render_template('homepage-new.html')
        
#login page
@app.route('/login', methods=['POST'])
def do_admin_login():
    #if request.form['password'] == 'password' and request.form['username'] == 'admin':
    #    session['logged_in'] = True
    #else:
    #    flash('wrong password!')
    return render_template('login.html')

# handle form data from hopepage
@app.route('/get-timeline-data', methods=['POST'])
def handle_timeline_data():
    #rows = connect("SELECT audioLink FROM chronological_view;")
    rows = connect("SELECT * FROM chronological_view;")
    return render_template('timeline.html',rows=rows)
    
    
    
# TEST TO DISPLAY USERS
@app.route('/get-user-data', methods=['POST'])
def handle_user_data():
    #retrieves data based on hardcoded SQL query 
    rows = connect("SELECT * FROM users;")
    #print('This is standard output', file=sys.stdout)

    return render_template('timeline.html',rows=rows)    
    
# handle form data from hopepage
@app.route('/get-custom-data', methods=['POST'])
def handle_custom_data():
    #rows = connect("SELECT audioLink FROM chronological_view;")
    rows = connect("SELECT * FROM chronological_view;")
    data = (request.form)
    name = 0
    date = 0
    size = 0
    player = 0
    if('file_name_box' in data):
        name = 1
    if('file_date_box' in data):
        date = 1
    if('file_size_box' in data):
        size = 1
    if('audio_player_box' in data):
        player = 1
    return render_template('timeline2.html',rows=rows, name = name, date=date,size=size,player=player)    
  
    

if __name__ == '__main__':
    #app.secret_key = os.urandom(12)
    app.run(debug = True)
    
    
    
    
