# Set a value for age (can be changed to test different cases)
age = 25

# Determine the stage of life based on the age
if age < 2:
    # Age less than 2 means the person is a baby
    print("The person is a baby.")
elif age < 4:
    # Age between 2 and 3 means toddler
    print("The person is a toddler.")
elif age < 13:
    # Age between 4 and 12 means kid
    print("The person is a kid.")
elif age < 20:
    # Age between 13 and 19 means teenager
    print("The person is a teenager.")
elif age < 65:
    # Age between 20 and 64 means adult
    print("The person is an adult.")
else:
    # Age 65 and above means elder
    print("The person is an elder.")
