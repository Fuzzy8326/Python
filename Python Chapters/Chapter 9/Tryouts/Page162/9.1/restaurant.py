# Define a class called Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant with a name and type of cuisine."""
        self.restaurant_name = restaurant_name  # Store the restaurant's name
        self.cuisine_type = cuisine_type        # Store the type of cuisine

    def describe_restaurant(self):
        """Print the restaurant's name and the cuisine it serves."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


# Create an instance of the Restaurant class
restaurant = Restaurant("The Curry Spot", "Indian")

# Print the attributes individually
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
