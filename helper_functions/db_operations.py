import os
from flask import request
from bson.objectid import ObjectId

from app import MONGO

# from helper_functions import data_manipulation as data_mnpt

bookings = MONGO.db.stora_bookings
units = MONGO.db.stora_units


def create_booking(submitted_form: dict):
    """
    Creates new booking to the database
    """
    bookings.insert_one(submitted_form)


def create_unit(submitted_form: dict):
    """
    Creates new dog to the database
    """
    units.insert_one(submitted_form)

def get_all_units():
    """
    Gets all units available
    """
    return units.find()
