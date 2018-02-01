# This program demonstrates the difference between strings,
# integers, doubles and booleans.

character_name = "Reza" # This is a string
character_health = 100  # This is an int
character_mana = 100.0  # This is a float
character_alive = True  # This is a boolean
character_level = "4"   # Although this is a number, it is still recognized as a string

# Integer plus a float
print(character_health + character_mana)

my_coins_int = 8000+5
my_coins_string = "8000 + 5"

# Printing with a comma suppresses the automatic new line
print(my_coins_int, my_coins_string)

print("\nThis will be printed on a new line")
print("\tThis is tabbed in")
print("\"This will be put in quotation marks in your string\"")

multi_line_string = """\nI am the night man
Destroyer of All Things Good
Protector of Spiders"""

# Prints multi line string
print(multi_line_string)

# We can attach two strings with concatenation.
print(character_name + character_level)