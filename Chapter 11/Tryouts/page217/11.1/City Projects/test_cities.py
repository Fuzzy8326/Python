# test_cities.py

# Import the function we want to test from city_functions module
from city_functions import city_country

def test_city_country():
    """
    Test that city_country() returns correctly formatted 'City, Country' string.
    """
    # Call the function with lowercase inputs
    result = city_country('santiago', 'chile')
    
    # Check if the result matches the expected formatted string
    assert result == 'Santiago, Chile'
