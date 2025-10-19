#Start with the basic function (from user_profile.py):
# user_profile.py

# Define a function that builds a user profile
# Accepts first and last names, plus any number of additional key-value pairs
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    
    # Create an empty dictionary to store the profile
    profile = {}
    
    # Add first and last name to the profile
    profile['first_name'] = first
    profile['last_name'] = last
    
    # Add any other key-value pairs provided in user_info
    for key, value in user_info.items():
        profile[key] = value
    
    # Return the complete profile dictionary
    return profile


#Build a profile of yourself using build_profile()
# my_profile.py

# Import the build_profile function from user_profile.py
from user_profile import build_profile

# Call the function to create a profile with first name, last name,
# and three additional pieces of information
my_profile = build_profile(
    'Fuzzy',                      # First name
    'Syed',                       # Last name
    location='Durban',         # Additional info: location
    field='Software Development',# Additional info: field of work
    hobby='Travel'          # Additional info: personal hobby
)

# Print the profile dictionary
print(my_profile)
