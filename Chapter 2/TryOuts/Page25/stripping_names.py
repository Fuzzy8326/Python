# 2-7. Stripping Names
# Define a string with leading and trailing whitespace, including tabs (\t) and newlines (\n)
name_with_whitespace = "\t\n  Ada Lovelace  \n\t"

# Print the original string using repr() to make whitespace characters visible
print("Original:", repr(name_with_whitespace))

# Use lstrip() to remove leading whitespace (spaces, tabs, newlines)
print("lstrip():", repr(name_with_whitespace.lstrip()))

# Use rstrip() to remove trailing whitespace (spaces, tabs, newlines)
print("rstrip():", repr(name_with_whitespace.rstrip()))

# Use strip() to remove both leading and trailing whitespace
print("strip():", repr(name_with_whitespace.strip()))
