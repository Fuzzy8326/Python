# Start an infinite loop to keep asking the user for pizza toppings
while True:
    # Prompt the user to enter a topping or 'quit' to stop adding toppings
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    
    # Check if the user wants to quit (case-insensitive)
    if topping.lower() == 'quit':
        # Print a closing message
        print("Finished adding toppings.")
        break  # Exit the infinite loop
    
    # If the user did not type 'quit', confirm the topping was added
    print(f"Adding {topping} to your pizza.")
