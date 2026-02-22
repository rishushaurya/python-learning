# A collection is like a toy box that holds many toys (values).
# There are 3 main toy boxes in Python:

# List = []  (like a row of toys) → ordered, you can change it, and you can have the same toy twice.
# Set  = {}  (like a messy basket) → not ordered, you can add/remove toys, but no duplicates allowed.
# Tuple = () (like a locked row of toys) → ordered, but you cannot change it. Faster to use.
#dictionary



# Let's play with a list of fruits:
#fruits = ["apple", "orange", "banana", "coconut"]



# print(dir(fruits))   # tells you what actions you can do with fruits

# Show the help guide
# print(help(fruits))   # explains what each action does

# Count how many toys are inside
# print(len(fruits))    # tells how many fruits are in the box

# Check if a toy is inside the box
# print("pineapple" in fruits)   # True if pineapple is there, False if not


# Check if a toy (fruit) is inside the box
#print("pineapple" in fruits)   # False, because pineapple is not there

# Change the first toy
#fruits[0] = "pineapple"        # apple becomes pineapple

# Add a new toy at the end
#fruits.append("pineapple")     # adds pineapple at the end

# Remove a toy
#fruits.remove("orange")        # removes orange

# Put a toy at the front
#fruits.insert(0, "grapes")     # adds grapes at position 0

# Sort toys alphabetically
#fruits.sort()                  # puts them in order

# Reverse the order
#fruits.reverse()               # flips the order

# Clear the box (remove all toys)
# fruits.clear()

# Find where a toy is
#print(fruits.index("banana"))  # tells the position of banana

# Count how many times a toy appears
#print(fruits.count("pineapple"))  # counts pineapples

# Show all toys in the box
#print(fruits)


fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)