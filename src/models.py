from flask_mongoengine import MongoEngine

db = MongoEngine()


class Unit(db.Document):
    """
    Class for defining structure of storage unit
    """

    unit_name = db.StringField(max_length=40, required=True)
    unit_size = db.StringField(max_length=40, required=True)
    unit_price = db.FloatField(required=True)

    meta = {"collection": "stora_units"}

    @staticmethod
    def get_available_unit_sizes():
        return map(lambda unit: unit.unit_size, Unit.objects.only("unit_size"))


class Booking(db.Document):
    """
    Class for defining structure of booking
    """

    user_name = db.StringField(max_length=40, required=True)
    address = db.StringField(max_length=40, required=True)
    email = db.EmailField(required=True)
    move_in_date = db.StringField(required=True)
    unit = db.ReferenceField(Unit, required=True)

    meta = {"collection": "stora_bookings"}
