# test_ncert_learn.py
import ncert_learn.intfncs as intfncs
import ncert_learn.stkdict as stkdict
import ncert_learn.mysql as mysql
import ncert_learn.area as area
import ncert_learn.conversions as conversions
import pytest

# Test for intfncs functions
def test_checkprime():
    assert intfncs.checkprime(5) == True
    assert intfncs.checkprime(4) == False

def test_factors():
    assert intfncs.factors(6) == [1, 2, 3, 6]
    assert intfncs.factors(13) == [1, 13]

# Test for stkdict functions
def test_createstackdict():
    stack = stkdict.createstackdict()
    assert stack == {}

# Test for area functions
def test_areaofcircle():
    assert round(area.areaofcircle(5), 4) == 78.5398

# Test for conversions functions
def test_integertobinary():
    assert conversions.integertobinary(10) == '1010'

# Test for MySQL connect (optional, use a mock or skip if no MySQL server is available)
def test_mysqlconnect():
    try:
        # Attempt to connect using the function in your module
        connection = mysql.mysqlconnect()

        # Check if the returned object is an instance of MySQLConnection
        assert isinstance(connection, mysql.connector.connection.MySQLConnection), "Returned object is not a MySQLConnection instance"

        # Close the connection after the test
        connection.close()

    except mysql.connector.Error as err:
        # If there's a connection error, pytest will skip this test
        pytest.skip(f"Cannot connect to MySQL: {err}")
