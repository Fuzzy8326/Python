# Define the User class to represent a user profile
class User:
    def __init__(self, first_name, last_name, **user_info):
        """
        Initialize the user with first and last names and optional additional attributes.
        :param first_name: str - user's first name
        :param last_name: str - user's last name
        :param user_info: dict - other optional user profile info as key-value pairs
        """
        self.first_name = first_name  # Store first name
        self.last_name = last_name    # Store last name
        self.user_info = user_info    # Store additional info as a dictionary

    def describe_user(self):
        """
        Print a summary of the user's profile information.
        Includes first and last name plus any other attributes.
        """
        print(f"User Profile for {self.first_name} {self.last_name}:")
        # Loop through all additional attributes and print them nicely
        for key, value in self.user_info.items():
            print(f"  {key.title()}: {value}")

    def greet_user(self):
        """
        Print a personalized greeting message for the user.
        """
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.\n")


# Create user instances with various profile data

user1 = User(
    "Alice",                     # First name
    "Johnson",                   # Last name
    age=28,                      # Additional attribute: age
    location="New York",         # Additional attribute: location
    profession="Data Scientist"  # Additional attribute: profession
)

user2 = User(
    "Bob",                       # First name
    "Smith",                     # Last name
    age=35,                      # Additional attribute: age
    location="San Francisco",    # Additional attribute: location
    hobby="Cycling"              # Additional attribute: hobby
)

user3 = User(
    "Charlie",                   # First name
    "Brown",                     # Last name
    age=22,                      # Additional attribute: age
    favorite_color="Blue",       # Additional attribute: favorite color
    pet="Dog"                    # Additional attribute: pet
)

# Call describe_user and greet_user methods for each user

user1.describe_user()  # Print Alice's profile summary
user1.greet_user()     # Greet Alice

user2.describe_user()  # Print Bob's profile summary
user2.greet_user()     # Greet Bob

user3.describe_user()  # Print Charlie's profile summary
user3.greet_user()     # Greet Charlie




