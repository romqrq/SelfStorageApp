from src.models import Booking, Unit


def test_new_unit():
    """
    GIVEN a Unit model
    WHEN creating a new unit
    THEN check key/values are defined correctly
    """
    unit = Unit(unit_name="test unit", unit_size="20", unit_price=20.20)
    assert unit.unit_name == "test unit"
    assert unit.unit_size == "20"
    assert unit.unit_price == 20.20


def test_new_booking():
    """
    GIVEN a Booking model
    WHEN creating a new booking
    THEN check key/values are defined correctly
    """
    booking = Booking(
        user_name="user name",
        address="user address",
        email="user email",
        move_in_date="move in date",
        unit=Unit(unit_name="test unit", unit_size="20", unit_price=20.20),
    )
    assert booking.user_name == "user name"
    assert booking.address == "user address"
    assert booking.email == "user email"
    assert booking.move_in_date == "move in date"
    assert booking.unit.unit_name == "test unit"
    assert booking.unit.unit_size == "20"
    assert booking.unit.unit_price == 20.20
