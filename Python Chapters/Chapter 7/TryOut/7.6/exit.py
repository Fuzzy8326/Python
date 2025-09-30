# Version 1: Using a variable initialized before the loop and checking condition in the while statement
topping = ''  # Initialize topping variable

# Loop until the user enters 'quit' (case-insensitive)
while topping.lower() != 'quit':
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
    # Only print the adding message if the input is not 'quit'
    if topping.lower() != 'quit':
        print(f"Adding {topping} to your pizza.")

# After the loop ends, print a finishing message
print("Finished adding toppings.")


# Version 2: Using a boolean flag to control the loop
active = True  # Flag to keep the loop running

# Loop while active is True
while active:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
    # If user types 'quit', set active to False to stop looping
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")

# After loop ends, print a finishing message
print("Finished adding toppings.")


# Version 3: Using an infinite loop with break to exit
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
    # Exit the loop immediately if user types 'quit'
    if topping.lower() == 'quit':
        break
    
    print(f"Adding {topping} to your pizza.")

# After breaking out of the loop, print a finishing message
print("Finished adding toppings.")

