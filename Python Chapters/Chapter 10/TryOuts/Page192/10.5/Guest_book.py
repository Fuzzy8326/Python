from pathlib import Path  # Import the Path class from the pathlib module

# Create a Path object pointing to the exact file location
path = Path('C:/Users/Fuzzy/Downloads/Python Classwork/Chapter 10/TryOuts/Page192/10.5/Guest_book.txt')

# Create an empty list to store names
guest_names = []

# Start a while loop to collect names
while True:
    name = input("Enter your name (or type 'quit' to finish): ")

    if name.lower() == 'quit':
        break  # Exit the loop if user types 'quit'

    guest_names.append(name)  # Add the name to the list
    print(f"Hello, {name}! You've been added to the guest book.")

# After the loop, join all names with newline characters and write them to the file
all_names = "\n".join(guest_names)  # Combine all names into a single string, one per line
path.write_text(all_names)  # Write the combined string to the file

# Notify the user
print("All guest names have been written to guest_book.txt.")
