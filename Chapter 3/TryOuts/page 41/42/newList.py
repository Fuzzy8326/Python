# Initial list of guests invited to dinner
guest = ['Selina', 'Joann', 'Kimberly', 'Kerusha']

# Identify the guest who cannot attend (second guest in the list)
unable_to_attend = guest[1]
print(f"\nUnfortunately, {unable_to_attend} can't make it to the dinner.")

# Replace the unavailable guest with a new guest named "Taybah"
guest[1] = "Taybah"

# Send updated invitations to all guests
print(f"Dear {guest[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guest[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guest[2]}, I would be honored to have you join me for dinner.")
print(f"Dear {guest[3]}, I would be honored to have you join me for dinner.")

