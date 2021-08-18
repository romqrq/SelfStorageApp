# import pytest
from src.app import create_app




def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid and data is correct
    """
    
    response = test_client.get("/")
    # print('-----------')
    # print(response.data.decode('utf-8'))
    # print('-----------')
    assert response.status_code == 200
        # --> Check what comes from response.data <--
        # assert b"Welcome to the Flask User Management Example!" in response.data
        # assert b"Need an account?" in response.data
        # assert b"Existing user?" in response.data


# def test_admin_page(test_client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/admin/units/new' page is requested (GET)
#     THEN check that the response is valid and data is correct
#     """

#     response = test_client.get('/admin/units/new')
#     assert response.status_code == 200


# def test_add_unit():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/admin/units/new' page is posted to (POST)
#     THEN check that the response is valid and data is correct
#     """
#     flask_app = create_app('flask_test.cfg')

#     with flask_app.test_client() as test_client:
#         response = test_client.get('/admin/units/new')
#         assert response.status_code == 200


# def test_get_add_booking():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/bookings/new/<unit_id' page is requested (GET)
#     THEN check that the response is valid and data is correct
#     """
#     flask_app = create_app('flask_test.cfg')

#     with flask_app.test_client() as test_client:
#         response = test_client.get('/bookings/new/<unit_id>') # To do set ID
#         assert response.status_code == 200


# def test_add_booking(): #test for get and post or overlap with submit_booking?
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/bookings/new/<unit_id>' page is posted to (POST)
#     THEN check that the response is valid and data is correct
#     """
#     flask_app = create_app('flask_test.cfg')

#     with flask_app.test_client() as test_client:
#         response = test_client.get('/bookings/new/<unit_id>') # To do set ID
#         assert response.status_code == 200


# def test_submit_booking():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/bookings/new/<unit_id>' page is posted to (POST)
#     THEN check that the response is valid and data is correct
#     """
#     flask_app = create_app('flask_test.cfg')

#     with flask_app.test_client() as test_client:
#         response = test_client.get('/bookings/new/<unit_id>') # To do set ID
#         assert response.status_code == 200

#test for 405 when trying not allowed method?
        