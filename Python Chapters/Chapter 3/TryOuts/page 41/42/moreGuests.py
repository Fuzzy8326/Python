# Initial list of guests invited to dinner
guest = ['Selina', 'Joann', 'Kimberly', 'Kerusha']

# Inform guests about finding a bigger dinner table
print("Good news! I found a bigger dinner table.\n")

# Add new guests to different positions in the list:
guest.insert(0, "Diana")    # Add "Diana" at the beginning of the list
guest.insert(2, "Edward")   # Add "Edward" at index 2 (middle of the list)
guest.append("Fiona")       # Add "Fiona" at the end of the list

# Send updated dinner invitations to all guests
print(f"Dear {guest[0]}, you are invited to dinner at my place!")
print(f"Dear {guest[1]}, you are invited to dinner at my place!")
print(f"Dear {guest[2]}, you are invited to dinner at my place!")
print(f"Dear {guest[3]}, you are invited to dinner at my place!")
print(f"Dear {guest[4]}, you are invited to dinner at my place!")
print(f"Dear {guest[5]}, you are invited to dinner at my place!")
