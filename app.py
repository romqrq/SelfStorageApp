# Importing libraries
import os
from os import path
from re import DEBUG
from typing import List
from dns.rdatatype import NULL
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if path.exists('env.py'):
    import env

DEBUG = False

# Creating instance of Flask
APP = Flask(__name__)
APP.secret_key = os.environ.get('SECRET_KEY')

# Adding Mongo database name and URI linking to that database.
APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

# Creating an instance of PyMongo
MONGO = PyMongo(APP)

# Importing helper functions
from helper_functions import data_manipulation as data_mnpt, db_operations as db_op


@APP.route('/')
def user_home():
    """ 
    Main page where users can choose where to go
    """
    return render_template('pages/index.html')


@APP.route('/bookings', methods=['GET', 'POST'])
def book_units():
    """ 
    Function to display booking form
    """

    return render_template('pages/bookings.html',
                            available_units_sizes=data_mnpt.build_list_with_storage_sizes())


@APP.route('/units', methods=['GET', 'POST'])
def get_units():
    """ 
    Function to display booking form
    """

    return render_template('pages/units.html',
                            units=db_op.get_all_units())


@APP.route('/admin', methods=['GET', 'POST'])
def admin_page():
    """ 
    Function to display admin form.
    """
    
    return render_template('pages/admin.html',
                            units=db_op.get_all_units())


@APP.route('/admin/units/new', methods=['GET', 'POST'])
def add_unit():
    """ Function to load the dashboard where users can update their account
    details or delete their account."""
    if request.form:

        # Test can be cadded here to check if entry already exists

        db_op.create_unit(request.form.to_dict())
   
        flash('Unit successfully created!', 'info')
    else:
        flash('Oops! Something went wrong, please try again.', 'info')

    return redirect(url_for('user_home'))


@APP.route('/bookings/new', methods=['POST'])
def add_booking():
    """ 
    Function to create new booking.
    """
    if request.form:

        # Test can be cadded here to check if entry already exists

        db_op.create_booking(request.form.to_dict())
   
        flash('Booking successfully created!', 'info')
    else:
        flash('Oops! Something went wrong, please try again.', 'info')

    return redirect(url_for('user_home'))


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
