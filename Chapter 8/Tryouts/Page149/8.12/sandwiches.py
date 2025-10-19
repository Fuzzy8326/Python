# Define a function that accepts any number of sandwich items
def make_sandwich(*items):
    # Print a summary of the sandwich order
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f" - {item}")

# Call 1: Sandwich with two items
make_sandwich("palony", "cheese")

# Call 2: Sandwich with four items
make_sandwich("turkey", "lettuce", "tomato", "mayo")

# Call 3: Sandwich with one item
make_sandwich("peanut butter")
