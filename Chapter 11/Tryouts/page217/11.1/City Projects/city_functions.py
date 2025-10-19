# city_functions.py

def city_country(city, country):
    """
    Return a formatted string with city and country names.

    Args:
        city (str): The name of the city.
        country (str): The name of the country.

    Returns:
        str: A string in the format 'City, Country' with title case.
    """
    # Format both city and country to title case and return them as 'City, Country'
    return f"{city.title()}, {country.title()}"
