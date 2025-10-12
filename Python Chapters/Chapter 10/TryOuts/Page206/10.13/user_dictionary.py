import json
from pathlib import Path

# Define the file path
path = Path("user_info.json")

# Check if we already have the user's info saved
if path.exists():
    try:
        # Read and load the JSON data
        contents = path.read_text()
        user_info = json.loads(contents)

        # Print what the program remembers about the user
        print("\nWelcome back!")
        print("Here's what I remember about you:")
        print(f"Name: {user_info['name']}")
        print(f"Age: {user_info['age']}")
        print(f"Favorite color: {user_info['favorite_color']}")
    except json.JSONDecodeError:
        # Handle case where file is empty or corrupted
        print("Hmm, I couldn't read your saved data. Let's try again.")
        user_info = {}
else:
    user_info = {}

# If no info was loaded, prompt for new input
if not user_info:
    name = input("What's your name? ")
    age = input("How old are you? ")
    favorite_color = input("What's your favorite color? ")

    # Store data in a dictionary
    user_info = {
        "name": name,
        "age": age,
        "favorite_color": favorite_color
    }

    # Convert dictionary to JSON and save it
    contents = json.dumps(user_info)
    path.write_text(contents)

    print("\nThanks! I've saved your information.")
