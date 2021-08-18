import pytest

from src.app import create_app
from src.models import Booking, Unit


def create_unit():
    return Unit(unit_name='test unit', unit_size='20', unit_price=20.20)


@pytest.fixture()
def new_unit():
    """
    GIVEN a Unit model
    WHEN creating a new unit
    THEN check key/values are defined correctly
    """
    return create_unit()


@pytest.fixture()
def test_new_booking():
    """
    GIVEN a Booking model
    WHEN creating a new booking
    THEN check key/values are defined correctly
    """
    return Booking(user_name='user name', address='user address', email='user email',
                move_in_date='move in date', unit=create_unit() )


@pytest.fixture()
def test_client():
    flask_app = create_app(test=True)

    with flask_app.test_client() as testing_client:
        # yield testing_client -> tried running client without the context manager
        with flask_app.app_context():
            yield testing_client

