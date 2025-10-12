import json
from pathlib import Path

# File to store the username
path = Path("username.json")


def get_stored_username():
    """Get the stored username if it exists."""
    if path.exists():
        try:
            contents = path.read_text()
            username = json.loads(contents)
            return username
        except json.JSONDecodeError:
            return None
    return None


def get_new_username():
    """Prompt the user to enter a new username and save it."""
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    return username


def greet_user():
    """Greet the user by name, confirming if the stored name is correct."""
    username = get_stored_username()

    if username:
        # Confirm if this is the current user
        print(f"Is your name {username}?")
        confirm = input("Enter 'yes' or 'no': ").strip().lower()

        if confirm == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"Thanks, {username}. We'll remember you next time!")
    else:
        # No user stored, ask for it
        username = get_new_username()
        print(f"Thanks, {username}. We'll remember you next time!")


# Run the program
greet_user()
