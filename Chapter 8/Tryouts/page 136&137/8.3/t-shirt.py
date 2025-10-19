# Define the function make_shirt with two parameters: size and message
def make_shirt(size, message):
    """Prints a summary of the shirt size and message."""
    # Print the size and message of the shirt
    print(f"The shirt size is {size} and it will have the message: '{message}' printed on it.")

# Call the function using positional arguments
# 'Medium' is passed as size, and 'Code like a pro!' as message
make_shirt("Medium", "Code like a pro!")

# Call the function using keyword arguments
# message is passed first, then size (order doesn't matter with keywords)
make_shirt(message="Dream big, code bigger!", size="Large")
