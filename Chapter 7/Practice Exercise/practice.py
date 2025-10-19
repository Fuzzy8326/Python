# Flag to control the loop
active = True

while active:
    user_input = input("Enter a number between 1 and 10 (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("You chose to quit. Exiting the loop.")
        break

    if user_input.isdigit():
        number = int(user_input)

        # Check if number is within the valid range
        if number < 1 or number > 10:
            print("Number is out of range. Try again.\n")
            continue

        if number == 5:
            print("You entered 5, exiting the loop.")
            break

        print(f"You entered: {number}\n")

    else:
        print("Invalid input. Please enter a number between 1 and 10 or 'quit'.\n")
        continue
