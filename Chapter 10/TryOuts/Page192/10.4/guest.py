from pathlib import Path  # Import the Path class from the pathlib module

# Create a Path object pointing to the exact file location
path = Path('C:/Users/Fuzzy/Downloads/Python Classwork/Chapter 10/TryOuts/Page192/10.4/guest.txt')

# Prompt the user to enter their name
name = input("What is your name? ")

# Write the name to the file specified by the Path object

path.write_text(name)

# Notify the user that their name has been written to the file
# f-string used for formatting the message
print(f"Your {name} name has been written to guest.txt")


