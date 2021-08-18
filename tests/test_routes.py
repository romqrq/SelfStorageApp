

def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid and data is correct
    """

    response = test_client.get("/")
    assert response.status_code == 200
    # assert content from response


def test_admin_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/admin/units/new' page is requested (GET)
    THEN check that the response is valid and data is correct
    """

    response = test_client.get("/admin/units/new")
    assert response.status_code == 200
    # assert content from response


def test_add_unit(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/admin/units/new' page is posted to (POST)
    THEN check that the response is valid and data is correct
    """
    response = test_client.get("/admin/units/new")
    assert response.status_code == 200
    # assert content from response
    # add and assert form submission


def test_get_add_booking(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/bookings/new/<unit_id' page is requested (GET)
    THEN check that the response is valid and data is correct
    """
    response = test_client.get("/bookings/new/<unit_id>")  # To do set ID
    assert response.status_code == 200
    # assert content from response


def test_submit_booking(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/bookings/new/<unit_id>' page is posted to (POST)
    THEN check that the response is valid and data is correct
    """
    response = test_client.get("/bookings/new/<unit_id>")  # To do set ID
    assert response.status_code == 200
    # assert content from response
    # add and assert form submission


# test for 405 when trying not allowed method
