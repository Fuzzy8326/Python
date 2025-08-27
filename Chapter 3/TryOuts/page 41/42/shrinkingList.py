# Starting guest list after adding more guests
guest= ['Diana', 'Selina', 'Edward', 'Joann', 'Kimberly', 'Kerusha', 'Fiona']

# Let everyone know about the change in plans
print("Unfortunately, the new dinner table won’t arrive in time, so I can invite only two people for dinner.\n")

# Remove guests one by one until only two remain

while len(guest) > 2:
    removed_guest = guest.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner this time.")


# Let the remaining two guests know they are still invited

print(f"{guest}, you are still invited to dinner!")

# Clear the list completely
del guest[0]
del guest[0]

# Print to confirm the list is now empty
print("\nFinal guest list:", guest)