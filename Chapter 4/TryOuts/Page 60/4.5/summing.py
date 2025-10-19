# Summing a million
# Create a list of numbers from 1 to 1,000,000 (inclusive)
million_numbers = list(range(1, 1000001))

# Verify the smallest number in the list (should be 1)
print(f"Min: {min(million_numbers)}")

# Verify the largest number in the list (should be 1,000,000)
print(f"Max: {max(million_numbers)}")

# Calculate and print the sum of all numbers in the list
print(f"Sum: {sum(million_numbers)}")
