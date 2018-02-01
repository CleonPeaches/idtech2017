import time
import sys


def print_intro():
    print("Welcome to the superhero database.")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)


def hero_search(dict):
    name = input("Enter a name or alias. Type \"1\" to exit: ")
    if name == "1":
        sys.exit
    elif name in dict:
        for i in len(dict):

    else:
        print("No matches found.")

superheroes = {"Clark Kent": "Superman"}
print_intro()
hero_search(superheroes)