# Create a dictionary to store people's favorite numbers
favorite_numbers = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 3,
    'Diana': 9,
    'Ethan': 13
}

# Loop through each key-value pair in the dictionary
for name, number in favorite_numbers.items():
    # Print the person's name and their favorite number using f-string
    print(f"{name}'s favorite number is {number}.")
