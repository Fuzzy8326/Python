#Writing Multiple Lines
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
contents += "I also love working with data.\n"

path = Path('C:/Users/Fuzzy/Downloads/Python Classwork/Chapter 10/programming.txt')
path.write_text(contents)

