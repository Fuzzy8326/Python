import json
from pathlib import Path

# Define the path to the file
path = Path("favorite_number.json")

# Try to read the favorite number from the file
if path.exists():
    try:
        # Read and parse the JSON data
        contents = path.read_text()
        fav_number = json.loads(contents)

        # Show the saved favorite number
        print(f"I know your favorite number! It's {fav_number}.")
    except json.JSONDecodeError:
        # If the file is corrupt or empty, treat it as no data
        fav_number = input("What is your favorite number? ")
        path.write_text(json.dumps(fav_number))
        print("Thanks! I've saved your favorite number.")
else:
    # If file doesn't exist, prompt and save
    fav_number = input("What is your favorite number? ")
    path.write_text(json.dumps(fav_number))
    print("Thanks! I've saved your favorite number.")
