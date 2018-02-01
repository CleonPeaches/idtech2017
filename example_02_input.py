# Takes input from user and assigns it to string variable character_name
character_name = input("What is your name, adventurer? ")
print("Hello, " + character_name + ".")

# Takes input from user and assigns it to int variable character_level
character_level = (input("What is your level, " + character_name + "? "))

# Checks if input is a positive number
if isinstance(character_level, int) == False or character_level <= 0:
 character_level = (input("Please enter a positive numeric value. "))


