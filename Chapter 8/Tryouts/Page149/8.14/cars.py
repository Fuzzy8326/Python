# Define a function to store car details in a dictionary
# 'manufacturer' and 'model' are required parameters
# '**car_info' collects any number of additional keyword arguments
def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    
    # Start by creating a dictionary with the required car info
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    
    # Loop through any additional keyword arguments and add them to the dictionary
    for key, value in car_info.items():
        car[key] = value
    
    # Return the complete car dictionary
    return car

# Call the function with required arguments and two additional details
car = make_car(
    'subaru',           # Manufacturer of the car
    'outback',          # Model of the car
    color='blue',       # Optional feature: color
    tow_package=True    # Optional feature: tow package
)

# Print the resulting dictionary to verify the information
print(car)
