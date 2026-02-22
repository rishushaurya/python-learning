result = input("Enter your full name: ")

# result = len(name)            # Length of the string (number of characters).
#                               # Useful for validation (e.g., password length).
#                               # ⚠️ Includes spaces and symbols, so "John Doe!" → 9.

# result = name.find("o")       # Index of first occurrence of "o".
#                               # Returns -1 if not found.
#                               # ⚠️ Case-sensitive: "O" won’t match lowercase "o".

# result = name.rfind("q")      # Index of last occurrence of "q".
#                               # Returns -1 if not found.
#                               # Useful for searching from the end of a string.

# name = name.capitalize()      # Capitalizes first letter, rest lowercase. 
#                               # Good for formatting names.
#                               # ⚠️ Only affects the first word: "john DOE" → "John doe".

# name = name.upper()           # Converts entire string to uppercase.
#                               # Useful for case-insensitive comparisons.
#                               # ⚠️ Loses original casing, so don’t use if you need exact formatting.

# name = name.lower()           # Converts entire string to lowercase.
#                               # Useful for normalization before comparison.
#                               # ⚠️ Same caveat: original casing is lost.

# result = name.isdigit()       # Checks if all characters are digits.
#                               # Useful for validating numeric input (like PIN codes).
#                               # ⚠️ Returns False if there are spaces or letters: "1234 " → False.

# result = name.isalpha()         # Checks if all characters are alphabetic.
#                               # Useful for validating names.
#                               # ⚠️ Returns False if spaces or symbols are included:
#                               # "JohnDoe" → True, "John Doe" → False.

result= result.replace("p" , "r") # replaces 


print(result)

# print(help(str)) #gives all 
