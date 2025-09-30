# Infinite loop to repeatedly ask for user input until they choose to quit
while True:
    # Prompt the user to enter their age or type 'quit' to exit
    age_input = input("Please enter your age (or type 'quit' to exit): ")
    
    # Check if the user wants to quit (case-insensitive)
    if age_input.lower() == 'quit':
        print("Thanks for visiting!")
        break  # Exit the loop
    
    # Check if the input consists only of digits (valid positive integer)
    if age_input.isdigit():
        age = int(age_input)  # Convert the input string to an integer
        
        # Determine ticket price based on age brackets
        if age < 3:
            price = 0  # Free ticket for babies under 3 years old
        elif 3 <= age <= 12:
            price = 10  # Child ticket price for ages 3 to 12
        else:
            price = 15  # Regular ticket price for everyone else
        
        # Print the corresponding ticket price message
        if price == 0:
            print("Your ticket is free!\n")
        else:
            print(f"Your ticket costs ${price}.\n")
    else:
        # Handle invalid input that is not a positive number or 'quit'
        print("Invalid input. Please enter a valid age or 'quit'.\n")
