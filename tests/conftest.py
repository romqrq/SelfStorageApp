import pytest
from flask import Blueprint, g
from src.app import create_app
from src.models import Unit, Booking

# bp = Blueprint('index_blueprint', __name__)

@pytest.fixture()
def test_client():
    flask_app = create_app(test=True)

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

            
def create_unit():
    return Unit('test unit', '20', 20.20)


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
    return Booking('user name', 'user address', 'user email', 'move in date',
                      unit=create_unit() )


