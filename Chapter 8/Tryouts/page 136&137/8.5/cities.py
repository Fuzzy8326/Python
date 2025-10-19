# Define a function that describes a city and its country
# The country parameter has a default value of "Iceland"
def describe_city(city, country="Iceland"):
    # Print a sentence stating where the city is located
    print(f"{city} is in {country}.")

# Call the function with only the city name; uses the default country
describe_city("Reykjavik")  # Output: Reykjavik is in Iceland.

# Call the function with another city name; still uses the default country
describe_city("Akureyri")   # Output: Akureyri is in Iceland.

# Call the function with both city and country to override the default
describe_city("Tokyo", "Japan")  # Output: Tokyo is in Japan.
