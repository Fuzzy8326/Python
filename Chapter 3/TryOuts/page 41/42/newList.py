guest= ['Selina','Joann','Kimberly','Kerusha']

#guest that cannot make it to dinner
unable_to_attend = guest[1]
print(f"\nUnfortunately, {unable_to_attend} can't make it to the dinner.")

# Replace the unavailable guest with a new one
guest[1] = "Taybah"

# Second round of invitations
print(f"Dear {guest[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guest[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guest[2]}, I would be honored to have you join me for dinner.")
print(f"Dear {guest[3]}, I would be honored to have you join me for dinner.")
