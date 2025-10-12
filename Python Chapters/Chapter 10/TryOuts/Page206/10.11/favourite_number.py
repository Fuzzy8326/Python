import json
from pathlib import Path

# Ask the user for their favorite number
fav_number = input("What is your favorite number? ")

# Convert to JSON format
number_json = json.dumps(fav_number)

# Define the path to the file
path = Path("favorite_number.json")

# Write the JSON data to the file
path.write_text(number_json)

print("Your favorite number has been saved.")
