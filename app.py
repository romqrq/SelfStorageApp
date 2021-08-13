import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_pymongo import PyMongo

from helper_functions import data_manipulation as data_mnpt
from helper_functions import db_operations as db_op

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
def user_home():
    """
    Main page where users can choose where to go
    """
    return render_template("pages/index.html")


@app.route("/bookings", methods=["GET", "POST"])
def book_units():
    """
    Function to display booking form
    """

    return render_template(
        "pages/bookings.html",
        available_units_sizes=data_mnpt.build_list_with_storage_sizes(),
    )


@app.route("/units", methods=["GET", "POST"])
def get_units():
    """
    Function to display booking form
    """

    return render_template("pages/units.html", units=db_op.get_all_units())


@app.route("/admin", methods=["GET", "POST"])
def admin_page():
    """
    Function to display admin form.
    """

    return render_template("pages/admin.html", units=db_op.get_all_units())


@app.route("/admin/units/new", methods=["GET", "POST"])
def add_unit():
    """Function to load the dashboard where users can update their account
    details or delete their account."""
    if request.form:
        db_op.create_unit(request.form.to_dict())

        flash("Unit successfully created!", "info")
    else:
        flash("Oops! Something went wrong, please try again.", "info")

    return redirect(url_for("user_home"))


@app.route("/bookings/new", methods=["POST"])
def add_booking():
    """
    Function to create new booking.
    """
    if request.form:
        db_op.create_booking(request.form.to_dict())

        flash("Booking successfully created!", "info")
    else:
        flash("Oops! Something went wrong, please try again.", "info")

    return redirect(url_for("user_home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=os.environ.get("PORT"), debug=False)
