# Define the function with default values for size and message
def make_shirt(size="Large", message="I love Python"):
    """Prints a summary of the shirt size and message."""
    print(f"The shirt size is {size} and it will have the message: '{message}' printed on it.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a custom shirt of any size with a different message
make_shirt(size="Small", message="Code more, worry less")
