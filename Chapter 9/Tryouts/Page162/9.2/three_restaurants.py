# Define a class to represent a restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant with a name and type of cuisine.
        :param restaurant_name: str - the name of the restaurant
        :param cuisine_type: str - the type of cuisine served
        """
        self.restaurant_name = restaurant_name  # Store restaurant name
        self.cuisine_type = cuisine_type        # Store cuisine type

    def describe_restaurant(self):
        """
        Print a description of the restaurant, including its name and cuisine type.
        """
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """
        Print a message indicating that the restaurant is open.
        """
        print(f"{self.restaurant_name} is now open!")


# Create the first instance of the Restaurant class
restaurant1 = Restaurant("The Curry Spot", "Indian")
# Create the second instance
restaurant2 = Restaurant("Bella Pasta", "Italian")
# Create the third instance
restaurant3 = Restaurant("Sushi World", "Japanese")

# Call the describe_restaurant() method for each instance
restaurant1.describe_restaurant()  # Output: The Curry Spot serves Indian cuisine.
restaurant2.describe_restaurant()  # Output: Bella Pasta serves Italian cuisine.
restaurant3.describe_restaurant()  # Output: Sushi World serves Japanese cuisine.