import os

from dotenv import dotenv_values
from flask import Flask, flash, redirect, render_template, request, url_for
from mongoengine import connect

from src.models import Booking, Unit, db


def create_app(test=False):
    config = dict()
    if test:
        config = dotenv_values(".env.test")
    else:
        config = dotenv_values(".env")

    mongo_uri = config.get("MONGO_URI")
    connect(host=mongo_uri)
    app = Flask(__name__)
    app.secret_key = config.get("SECRET_KEY")

    app.config["MONGO_DBNAME"] = config.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = mongo_uri
    app.config["PORT"] = config.get("PORT")
    app.config["TEST"] = test
    return app


app = create_app()


@app.route("/")
def user_home():
    """
    Main page where users can choose where to go
    """
    return render_template("/pages/index.html", units=Unit.objects())


@app.route("/admin/units/new", methods=["GET"])
def admin_page():
    """
    Function to display admin form.
    """

    return render_template("/pages/admin.html", units=Unit.objects())


@app.route("/admin/units/new", methods=["POST"])
def add_unit():
    """Function to load the dashboard where users can update their account
    details or delete their account."""
    try:
        unit = Unit(**request.form.to_dict())
        unit.save()
    except:
        flash("Oops! Something went wrong, please try again.", "info")
    else:
        flash("Unit successfully created!", "info")

    return redirect(url_for("user_home"))


@app.route("/bookings/new/<unit_id>", methods=["GET"])
def add_booking(unit_id):
    """
    Function to create new booking.
    """

    return render_template(
        "pages/bookings.html",
        sel_unit=Unit.objects.get(id=unit_id),
        all_units=Unit.objects(),
    )


@app.route("/bookings/new/<unit_id>", methods=["POST"])
def submit_booking(unit_id):
    """
    Function to submit new booking.
    """
    try:
        booking = Booking(**request.form.to_dict())
        booking.unit = Unit.objects.get(id=unit_id)
        booking.save()
    except:
        flash("Oops! Something went wrong, please try again.", "info")
    else:
        flash("Booking successfully created!", "info")

    return redirect(url_for("user_home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=os.environ.get("PORT"), debug=False)
