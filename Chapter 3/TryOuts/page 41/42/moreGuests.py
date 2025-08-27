guest= ['Selina','Joann','Kimberly','Kerusha']

# Informing guests that a bigger table has been found
print("Good news! I found a bigger dinner table.\n")

# Add new guests
guest.insert(0, "Diana")  # Beginning of the list
guest.insert(2, "Edward")  # Middle of the list
guest.append("Fiona")  # End of the list

# Send new invitations

print(f"Dear {guest[0]}, you are invited to dinner at my place!")
print(f"Dear {guest[1]}, you are invited to dinner at my place!")
print(f"Dear {guest[2]}, you are invited to dinner at my place!")
print(f"Dear {guest[3]}, you are invited to dinner at my place!")
print(f"Dear {guest[4]}, you are invited to dinner at my place!")
print(f"Dear {guest[5]}, you are invited to dinner at my place!")