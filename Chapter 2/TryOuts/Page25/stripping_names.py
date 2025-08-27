# 2-7. Stripping Names
name_with_whitespace = "\t\n  Ada Lovelace  \n\t"
print("Original:", repr(name_with_whitespace))

# Using stripping methods
print("lstrip():", repr(name_with_whitespace.lstrip()))
print("rstrip():", repr(name_with_whitespace.rstrip()))
print("strip():", repr(name_with_whitespace.strip()))
