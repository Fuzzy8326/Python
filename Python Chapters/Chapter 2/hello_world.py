#Concatenation: Combining two or more strings into one.
greeting = "Hello"
name = "Alice"
print("1. Concatenation:",greeting + " " + name)  

#Repetition: Repeating a string multiple times.
print("2. Repetition:", "Hello! " * 3) 

#Slicing: Extracting a portion of a string.
print("3. Slicing:", "Hello, World!"[7:12])  

#Escape Characters: Using special characters like newline (\n) and tab (\t).
print("4.Escape Characters: ","Line 1\nLine 2\n\tIndented Line")

#String Length: Using the len() function to find the length of a string.
print("5. String Length: ",len("Hello, Alice!"))  

#Indexing: Accessing individual characters in a string (starting from 0).
print("6.  Indexing:","Hello"[0])  

#Negative Indexing: Accessing characters from the end of the string.
print("7. Negative Indexing:","Hello"[-1]) 

#String Comparison: Comparing strings using comparison operators.
print("8. String Comparison:","apple" == "apple")  
###########################################################################
#upper(): Converts all characters to uppercase.
message = "hello, world"
print("9.Uppercase:", message.upper())  

#lower(): Converts all characters to lowercase.
message = "HELLO, WORLD"
print("10.Lowercase:",message.lower())  

#strip(): Removes leading and trailing whitespace.
message = "   Hello, World!   "
print("11. Removes leading whitespace:", message.strip())  
#replace(): Replaces one substring with another.
message = "Hello, World!"
print("12. Replaces Substring:",message.replace("World", "Alice"))  

#find(): Finds the index of the first occurrence of a substring.
message = "Hello, World!"
print("13. Finds Index: ", message.find("World"))  

#split(): Splits a string into a list(Array) based on a delimiter.
message = "apple,banana,cherry"
print("14. Splits String:",message.split("-"))  
