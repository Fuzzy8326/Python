# Starting guest list after adding more guests
guest = ['Diana', 'Selina', 'Edward', 'Joann', 'Kimberly', 'Kerusha', 'Fiona']

# Inform everyone about the change in dinner plans due to the new table not arriving on time
print("Unfortunately, the new dinner table won’t arrive in time, so I can invite only two people for dinner.\n")

# Remove guests one by one from the end of the list until only two guests remain
while len(guest) > 2:
    removed_guest = guest.pop()  # Remove the last guest from the list
    print(f"Sorry {removed_guest}, I can't invite you to dinner this time.")

# Notify the remaining two guests that they are still invited
print(f"{guest}, you are still invited to dinner!")

# Remove the remaining two guests from the list to clear it completely
del guest[0]  # Delete the first guest in the list
del guest[0]  # Delete the next guest (now at index 0 after previous deletion)

# Print the final guest list to confirm it's empty
print("\nFinal guest list:", guest)
