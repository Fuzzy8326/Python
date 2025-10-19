# Create a glossary dictionary with programming terms as keys and their meanings as values
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A control structure that repeats a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs in Python.',
    'list': 'An ordered collection of items in Python that can be changed.'
}

# Loop through each term and its definition in the glossary
for word, meaning in glossary.items():
    # Print the word with the first letter capitalized and its meaning indented
    print(f"{word.title()}:\n  {meaning}\n")





